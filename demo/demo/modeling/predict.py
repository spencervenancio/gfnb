from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from demo.config import MODELS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR

from sklearn.metrics import root_mean_squared_error
import joblib

import pandas as pd  

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "X_test_trans.csv",
    model_path: Path = MODELS_DIR / "model.joblib",
    predictions_path: Path = PROCESSED_DATA_DIR / "y_pred.csv",
    # -----------------------------------------
):
    # Load pretrained model
    model = joblib.load(model_path)

    # Make predictions with the model 
    X_test = pd.read_csv(features_path, index_col=0)
    y_pred = model.predict(X_test)

    # Save the prediction
    pd.Series(y_pred, index=X_test.index, name="target").to_csv(predictions_path)

    # Score against ground truth
    y_true = pd.read_csv(RAW_DATA_DIR / 'y_test.csv', index_col=0)["target"]
    rmse = root_mean_squared_error(y_true, y_pred)

    logger.info(f"{rmse=}")

    return None


if __name__ == "__main__":
    app()
