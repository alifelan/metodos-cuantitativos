from numpy.random import exponential, gamma, weibull, lognormal, pareto


def test(df):
    """Run each distribution on each column."""
    for column in df:
        print(exp(df[column]))
        print(gam(df[column]))
        print(wei(df[column]))
        print(logn(df[column]))
        print(pare(df[column]))
        input("Press enter to continue.")


def test_exp(df):
    """Run exponential distribution on each column."""
    print('Running Exponential test...')
    for column in df:
        print(exp(df[column]))
        input("Press enter to continue.")


def test_gam(df):
    """Run gamma distribution on each column."""
    print('Running Gamma test...')
    for column in df:
        print(gam(df[column]))
        input("Press enter to continue.")


def test_wei(df):
    """Run wei distribution on each column."""
    print('Running Weibull test...')
    for column in df:
        print(wei(df[column]))
        input("Press enter to continue.")


def test_logn(df):
    """Run logn distribution on each column."""
    print('Running Lognormal test...')
    for column in df:
        print(logn(df[column]))
        input("Press enter to continue.")


def test_pare(df):
    """Run pare distribution on each column."""
    print('Running Pareto test...')
    for column in df:
        print(pare(df[column]))
        input("Press enter to continue.")


def exp(df):
    """Exponential distribution."""
    return exponential(df)


def gam(df):
    """Gamma distribution."""
    return gamma(df)


def wei(df):
    """Weibull distribution."""
    weibull(df)


def logn(df):
    """Lognormal distribution."""
    lognormal(df)


def pare(df):
    """Pareto distribution."""
    pareto(df)
