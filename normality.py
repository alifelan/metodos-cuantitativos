from scipy.stats import anderson, kstest, shapiro
import pandas as pd


def test(df: pd.DataFrame):
    """Test each column with the methods."""
    for column in df:
        anderson(df[column])
        kstest_test(df[column])
        shapiro_test(df[column])


def anderson_test(data: pd.Series):
    """Run Anderson-Darling test on data received"""
    anderson(data)


def kstest_test(data: pd.Series):
    """Run Kolmogorov-Smirnov test on data received"""
    kstest(data, 'norm')


def shapiro_test(data: pd.Series):
    """Run Ryan-Joiner equivalent, Shapiro-Wilk test on data received"""
    shapiro(data)
