from data import read, filter, normalize
import pandas as pd
import normality
import distribution


def distribution_test(df: pd.DataFrame = pd.DataFrame()):
    if df.empty:
        df = filter(read())
    distribution.test_exp(df)
    distribution.test_gam(df)
    distribution.test_wei(df)
    distribution.test_logn(df)
    distribution.test_pare(df)


def normality_test(df: pd.DataFrame = pd.DataFrame()):
    if df.empty:
        df = filter(read())
    normality.test_and(df)
    normality.test_ks(df)
    normality.test_sh(df)


def main():
    df = normalize(filter(read()))
    print('Running normality tests...')
    normality_test(df)
    print('Running distribution tests...')
    distribution_test(df)


if __name__ == '__main__':
    main()
