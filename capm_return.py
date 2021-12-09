"""
Calculate CAPM using pandas
"""
import pandas as pd


def capm_return():
    """Calculates the CAPM return and prints the results along the way"""
    # AAPL, TSLA
    data = {
        "AAPL": [
            74.095229157816846,
            73.374876006024522,
            73.959546201143638,
            73.611704439490481,
            74.795846606820334,
        ],
        "TSLA": [
            86.052000000000007,
            88.602000000000004,
            90.308000000000007,
            93.812000000000012,
            98.427999999999997,
        ],
        "SPY": [
            315.68826255969481,
            313.29778905984301,
            314.49302580976888,
            313.60874496226279,
            315.28013293776888,
        ],
    }
    print("--- PRICES ---")
    df_prices = pd.DataFrame(data)
    print(df_prices)

    print("--- RETURNS ---")
    df_pct_change = df_prices.pct_change()
    print(df_pct_change)

    print("--- COVARIANCE MATRIX ---")
    df_cov = df_pct_change.cov()
    print(df_cov)

    print("--- BETAS ---")
    betas = df_cov["SPY"] / df_cov.loc["SPY", "SPY"]
    print(betas)
    print("Remove unwanted row")
    betas = betas.drop("SPY")
    print(betas)


if __name__ == "__main__":
    capm_return()
