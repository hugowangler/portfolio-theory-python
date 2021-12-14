"""
Tests betas implementation
"""
import pandas as pd
from data.test import DF_DATA
from capm_return import returns


def betas(prices: pd.DataFrame, market_ticker: str = "SPY"):
    """Calculates the covariance between a stock and the market (SPY)"""
    df_ret = returns(prices)
    betas = df_ret.apply(lambda row: calc_beta(row, df_ret[market_ticker]))
    return betas


def calc_cov(returns: pd.DataFrame, market_returns: pd.DataFrame) -> float:
    return (
        (returns - returns.mean()) * (market_returns - market_returns.mean())
    ).sum() / (len(returns) - 1)


def calc_beta(returns: pd.DataFrame, market_returns: pd.DataFrame) -> float:
    return calc_cov(returns, market_returns) / calc_cov(
        market_returns, market_returns
    )


def betas_pandas(prices: pd.DataFrame, market_ticker: str = "SPY"):
    """
    Assmues that the column containing the market returns are labeled
    according to marketTicker in returns DataFrame
    """
    df_ret = returns(prices)
    cov = df_ret.cov()
    betas = cov[market_ticker] / cov.loc[market_ticker, market_ticker]
    # return betas.drop(market_ticker)
    return betas


if __name__ == "__main__":
    print("--- DATA ---")
    print(DF_DATA)
    print("--- MEANS ---")
    df_ret = returns(DF_DATA)
    print(df_ret.mean())
    print("--- COVARIANCE MATRIX (PANDAS) ---")
    print(df_ret.cov())
    print("--- PANDAS CALCULATED BETAS ---")
    print(betas_pandas(DF_DATA))
    print("--- OWN FORMULA BETAS ---")
    print(betas(DF_DATA))
