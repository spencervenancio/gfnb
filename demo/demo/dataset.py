# Imports
import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

from pathlib import Path

import typer

from demo.config import RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    output_dir: Path = RAW_DATA_DIR 
):
    # Load Dataset 
    df = load_diabetes(as_frame=True)
    X = df['data']
    y = df['target']

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Save to the PROCESSED_DATA_DIR
    X_train.to_csv(output_dir / "X_train.csv")
    X_test.to_csv(output_dir / "X_test.csv")
    y_train.to_csv(output_dir / "y_train.csv")
    y_test.to_csv(output_dir / "y_test.csv")

if __name__ == "__main__":
    app()