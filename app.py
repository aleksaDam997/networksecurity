import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_DATABASE=os.getenv("DB_DATABASE")
DB_TABLE=os.getenv("DB_TABLE")
DB_PORT=os.getenv("DB_PORT")

import certifi
certifi.where()

import pandas as pd
import numpy as np
import mysql.connector
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.model.estimator import NetworkModel

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse

from networksecurity.utils.main_utils.utils import load_object



from networksecurity.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME, DATA_INGESTION_TABLE_NAME

app = FastAPI()


conn = None

@app.on_event("startup")
def startup():
    global conn
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        port=DB_PORT
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successfull...")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
import os

@app.post("/predict", response_class=HTMLResponse)
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        df.columns = df.columns.str.strip()
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")

        network_model = NetworkModel(
            preprocessor=preprocessor,
            model=final_model
        )

        y_pred = network_model.predict(df)
        df["predicted_column"] = y_pred

        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/output.csv", index=False)

        table_html = df.to_html(classes="table table-striped", index=False)

        return templates.TemplateResponse(
            "table.html", {"request": request, "table": table_html}
        )

    except Exception as e:
        logging.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)