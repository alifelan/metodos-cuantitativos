from numpy.random import exponential, gamma, weibull, lognormal, pareto


def test(df):
    """Run each distribution on each column."""
    for colummn in df:
        exp(df[column])
        gam(df[colummn])
        wei(df[colummn])
        logn(df[colummn])
        pare(df[column])


def exp(df):
    """Exponential distribution."""
    exponential(df)


def gam(df):
    """Gamma distribution."""
    gamma(df)


def wei(df):
    """Weibull distribution."""
    weibull(df)


def logn(df):
    """Lognormal distribution."""
    lognormal(df)


def pare(df):
    """Pareto distribution."""
    pareto(df)
