from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys

def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    try:
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted')
        recall = recall_score(y_true, y_pred, average='weighted')
        f1 = f1_score(y_true, y_pred, average='weighted')

        classification_metric_artifact = ClassificationMetricArtifact(
            accuracy=accuracy,
            precision=precision,
            recall=recall,
            f1_score=f1
        )

        return classification_metric_artifact
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e