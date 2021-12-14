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
    return pd.DataFrame(prices.pct_change().dropna(how="all"))


def capm_return(
    prices: pd.DataFrame,
    market_ticker: str = "SPY",
    risk_free_rate: float = 0.02,
    compounding: bool = True,
) -> pd.DataFrame:
    """Calculates the CAPM return and prints the results along the way"""
    frequency = len(prices[market_ticker])
    # AAPL, TSLA, SPY
    print("--- PRICES ---")
    print(prices)
    print("--- RETURNS ---")
    df_ret = returns(prices)
    print(df_ret)

    print("--- COVARIANCE MATRIX ---")
    df_cov = df_ret.cov()
    print(df_cov)

    print("--- BETAS ---")
    betas = df_cov["SPY"] / df_cov.loc["SPY", "SPY"]
    print(betas)
    betas = betas.drop("SPY")

    if compounding:
        # Geometric mean returns
        mkt_mean_ret = (1 + df_ret[market_ticker]).prod() ** (
            frequency / df_ret[market_ticker].count()
        ) - 1
    else:
        # Arithmetic mean returns
        mkt_mean_ret = df_ret[market_ticker].mean() * frequency

    return risk_free_rate + betas * (mkt_mean_ret - risk_free_rate)


if __name__ == "__main__":
    capm = capm_return(DF_DATA)
    print("--- CAPM RETURN ---")
    print(capm)
