"""
Tests betas implementation
"""
import pandas as pd
from data.test import DF_DATA


def betas(returns: pd.DataFrame, market_ticker: str = "SPY"):
    """Calculates the covariance between a stock and the market (SPY)"""
    betas = returns.apply(lambda row: calc_beta(row, returns[market_ticker]))
    return betas


def calc_cov(returns, market_returns):
    return (
        (returns - returns.mean()) * (market_returns - market_returns.mean())
    ).sum() / (len(returns) - 1)


def calc_beta(returns, market_returns):
    return calc_cov(returns, market_returns) / calc_cov(
        market_returns, market_returns
    )


def betas_pandas(returns: pd.DataFrame, market_ticker: str = "SPY"):
    """
    Assmues that the column containing the market returns are labeled
    according to marketTicker in returns DataFrame
    """
    cov = returns.cov()
    betas = cov[market_ticker] / cov.loc[market_ticker, market_ticker]
    # return betas.drop(market_ticker)
    return betas


if __name__ == "__main__":
    print("--- DATA ---")
    print(DF_DATA)
    print("--- PANDAS CALCULATED BETAS ---")
    print(betas_pandas(DF_DATA))
    print("--- OWN FORMULA BETAS ---")
    print(betas(DF_DATA))
