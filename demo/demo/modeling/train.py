from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from demo.config import MODELS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR

import pandas as pd

from sklearn.linear_model import LinearRegression
import joblib


app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "X_train_trans.csv",
    labels_path: Path = RAW_DATA_DIR / "y_train.csv",
    model_path: Path = MODELS_DIR / "model.joblib",
    # -----------------------------------------
):
    X_train = pd.read_csv(features_path, index_col=0)
    y_train = pd.read_csv(labels_path, index_col=0)["target"]

    # Train the Linear Regression Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, model_path)

    return None


if __name__ == "__main__":
    app()
