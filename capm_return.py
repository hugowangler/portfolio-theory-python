"""
Calculate CAPM using pandas
"""
import pandas as pd

from data.test import DF_DATA


def returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates and returns a DataFrame containing the returns of a ticker
    given the prices
    """
    return prices.pct_change()


def capm_return(returns: pd.DataFrame):
    """Calculates the CAPM return and prints the results along the way"""
    # AAPL, TSLA, SPY
    print("--- RETURNS ---")
    print(returns)

    print("--- COVARIANCE MATRIX ---")
    df_cov = returns.cov()
    print(df_cov)

    print("--- BETAS ---")
    betas = df_cov["SPY"] / df_cov.loc["SPY", "SPY"]
    print(betas)
    print("Remove unwanted row")
    betas = betas.drop("SPY")
    print(betas)


if __name__ == "__main__":
    capm_return(DF_DATA)
