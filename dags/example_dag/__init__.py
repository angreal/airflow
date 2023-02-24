import logging
from random import randint

from airflow.models.taskinstance import TaskInstance

log = logging.getLogger()

def _choosing_best_model(ti: TaskInstance):
    """Given a set of accuracies, determine if any model is 'accurate' or not. """
    accuracies = ti.xcom_pull(
        task_ids=["training_model_A", "training_model_B", "training_model_C"]
    )
    if max(accuracies) > 8:
        return "accurate"
    return "inaccurate"


def _train_model(model):
    """model training returns a model score between 1 and 10 """
    logging.info(f"generating accuracy score for model {model}")
    return randint(1, 10)
