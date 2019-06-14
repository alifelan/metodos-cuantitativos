from scipy.stats import anderson, kstest, shapiro
import pandas as pd


def test(df: pd.DataFrame):
    """Test each column with the methods."""
    print('Testing normality...')
    for column in df:
        print(anderson_test(df[column]))
        print(kstest_test(df[column]))
        print(shapiro_test(df[column]))
        input("Press enter to continue.")


def test_and(df: pd.DataFrame):
    """Test each column with anderson test."""
    print('Running Anderson-Darling test...')
    for column in df:
        print(anderson(df[column]))
        input("Press enter to continue.")


def test_ks(df: pd.DataFrame):
    """Test each column with ks test."""
    print('Running Kolmogorov-Smirnov test...')
    for column in df:
        print(kstest_test(df[column]))
        input("Press enter to continue.")


def test_sh(df: pd.DataFrame):
    """Test each column with shapiro test."""
    print('Running Shapiro-Wilk test...')
    for column in df:
        print(shapiro_test(df[column]))
        input("Press enter to continue.")


def anderson_test(data: pd.Series):
    """Run Anderson-Darling test on data received"""
    return anderson(data)


def kstest_test(data: pd.Series):
    """Run Kolmogorov-Smirnov test on data received"""
    return kstest(data, 'norm')


def shapiro_test(data: pd.Series):
    """Run Ryan-Joiner equivalent, Shapiro-Wilk test on data received"""
    return shapiro(data)
