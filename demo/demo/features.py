from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from demo.config import RAW_DATA_DIR, PROCESSED_DATA_DIR


import pandas as pd
from sklearn.preprocessing import StandardScaler

app = typer.Typer()


@app.command()
def main(
    input_dir: Path = RAW_DATA_DIR,
    output_dir: Path = PROCESSED_DATA_DIR,
):
    # Load Data
    train_path = input_dir / "X_train.csv"
    test_path = input_dir / "X_test.csv" 
    X_train = pd.read_csv(train_path, index_col=0)
    X_test = pd.read_csv(test_path, index_col=0)

    # Fit the scaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    # Scale the data
    X_train_transformed = pd.DataFrame(
        scaler.transform(X_train), columns=X_train.columns, index=X_train.index
    )
    X_test_transformed = pd.DataFrame(
        scaler.transform(X_test), columns=X_test.columns, index=X_test.index
    )

    # Save the transformed data
    X_train_transformed.to_csv(output_dir / "X_train_trans.csv")
    X_test_transformed.to_csv(output_dir / "X_test_trans.csv")

    return None

if __name__ == "__main__":
    app()
