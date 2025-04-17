from typing import Union
import numpy as np
import pandas as pd

def Simulate(n: int, cohort: str, stage: str, dataset: str, label: Union[int, str], sex: Union[int, str], measurement_type='FTIR') -> np.ndarray:
    """
    Simulates data using a multivariate Gaussian model based on the provided parameters.

    Parameters:
    -----------
    n : int
        The number of samples to generate.
    cohort : str
        The cohort name (e.g., 'luca', 'prca', etc.).
    stage : str
        The stage of the cohort (e.g., 'None', 'stage1', etc.).
    dataset : str
        The dataset type (e.g., 'train', 'test').
    label : int or str
        The label for the data (e.g., 0 or 1).
    sex : int or str
        The sex for the data (e.g., 0 or 1).
    measurement_type: 'FTIR' or 'FRS'

    Returns:
    --------
    np.ndarray
        A NumPy array containing the simulated data. If no model exists (mean and covariance are NaN), 
        the array will be filled with NaN values.

    Notes:
    ------
    - The function reads a pre-trained model (mean and covariance) from a Parquet file.
    - If the model does not exist (contains NaN values), the function returns an array of NaN values.
    - If the model exists, the function uses the mean and covariance to sample data using a multivariate Gaussian distribution.
    """

    # Construct the model name based on the input parameters
    model_name = f'{cohort}-{stage}-{dataset}-label{label}-sex{sex}'
    
    # Load the model (mean and covariance) from a Parquet file
    model = pd.read_parquet(f'./Models/{measurement_type}/{model_name}.parquet')

    # Check if the model contains NaN values (indicating no model exists)
    if bool(model.isna().values.any()):
        # If no model exists, return an array filled with NaN values
        X_hat = np.full((n, np.shape(model)[1]), np.nan)

    # If the model exists, use it to generate data
    else:
        # Extract the mean and covariance from the model
        model = model.values
        mean = model[0]  # First row is the mean
        cov = model[1:]  # Remaining rows are the covariance matrix

        # Generate data using a multivariate Gaussian distribution
        X_hat = np.random.multivariate_normal(mean, cov, n)

    return X_hat