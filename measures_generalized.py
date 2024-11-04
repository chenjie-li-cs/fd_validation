from typing import List, Any
import pandas as pd
import numpy as np
import math
import itertools
# co-occurence 

def rho_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    lhs_rhs_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    lhs_rhs_counts.columns = lhs + rhs + ["lhs_rhs_count"]
    lhs_counts = df.loc[:, lhs].value_counts().reset_index()
    return lhs_counts.shape[0] / lhs_rhs_counts.shape[0]

# g-measures
def g1_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
    violating_tuple_pairs = (
        (counts["xy_count"]) * (counts["x_count"] - counts["xy_count"])
    ).sum()
    return 1.0 - (violating_tuple_pairs / (df.shape[0] ** 2))


def g1_prime_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
    violating_tuple_pairs = (
        (counts["xy_count"]) * (counts["x_count"] - counts["xy_count"])
    ).sum()
    return 1.0 - (
        violating_tuple_pairs
        / ((df.shape[0] ** 2) - (xy_counts["xy_count"].pow(2)).sum())
    )


def shannon_g1_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure calculates 1 - H_R(Y|X), where H_R is the conditional Shannon entropy."""
    r_size = df.shape[0]
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
    print(f'counts["x_count"]: {counts["x_count"]}')
    shannonYX = (
        -1.0
        * (
            (counts["xy_count"] / r_size)
            * np.log2((counts["xy_count"] / r_size) / (counts["x_count"] / r_size))
        ).sum()
    )
    return 1 - shannonYX


def shannon_g1_plus_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """The baselined version of shannon_g1."""
    return max(0, shannon_g1_general(df, lhs, rhs))


def g2_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is g_2 as proposed by [Kivinen & Mannila, 1995](https://doi.org/10.1016/0304-3975(95)00028-U)."""
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
    violation_participating_tuples = counts[counts["x_count"] > counts["xy_count"]]
    return 1.0 - ((violation_participating_tuples["xy_count"] / df.shape[0]).sum())


def g3_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is g_3 as proposed by [Kivinen & Mannila, 1995](https://doi.org/10.1016/0304-3975(95)00028-U)."""
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_groups = xy_counts.groupby(lhs)["xy_count"]
    minimum_deletions_needed = (x_groups.sum() - x_groups.max()).sum()
    
    return 1.0 - (minimum_deletions_needed / df.shape[0])


def g3_prime_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is g_3 in its renormalized variant proposed by [Giannella & Robertson, 2003](https://doi.org/10.1016/j.is.2003.10.006)."""
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_groups = xy_counts.groupby(lhs)["xy_count"]
    minimum_deletions_needed = (x_groups.sum() - x_groups.max()).sum()
    return 1.0 - (minimum_deletions_needed / (df.shape[0] - df.loc[:, lhs].nunique())).values[0]

# fraction of information

def fraction_of_information_general(df: pd.DataFrame,  lhs: List[Any], rhs: List[Any]) -> float:
    """This measures matches the function FD as defined by [Cavallo & Pittarelli, 1987](https://dblp.org/rec/conf/vldb/CavalloP87)."""
    r_size = df.shape[0]
    y_counts = df.loc[:, rhs].value_counts().reset_index()
    y_counts.columns = rhs + ["y_count"]
    shannonY = (
        -1.0
        * ((y_counts["y_count"] / r_size) * np.log2(y_counts["y_count"] / r_size)).sum()
    )
    xy_counts = df.loc[:, lhs+rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs+["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
        
    shannonYX = (
        -1.0
        * (
            (counts["xy_count"] / r_size)
            * np.log2((counts["xy_count"] / r_size) / (counts["x_count"] / r_size))
        ).sum()
    )
    return (shannonY - shannonYX) / shannonY

def reliable_fraction_of_information_general(df: pd.DataFrame,  lhs: List[Any], rhs: List[Any]) -> float:
    """This measures is reliable fraction of information as defined by [Mandros, Boley & Vreeken, 2017](https://doi.org/10.1145/3097983.3098062)."""
    n = df.shape[0]
    x_counts = df.loc[:, lhs].value_counts()
    y_counts = df.loc[:, rhs].value_counts()
    m = 0.0
    for _, a in x_counts.items():
        comb_n_a = math.comb(n, a)
        for _, b in y_counts.items():
            k0 = max(0, a + b - n)
            p0 = math.comb(b, k0) * math.comb(n - b, a - k0) / comb_n_a
            if k0 != 0:
                m += p0 * (k0 / n) * math.log((k0 * n) / (a * b), 2)

            for k1 in range(k0 + 1, min(a, b) + 1):
                p0 = p0 * (((a - k0) * (b - k0)) / (k1 * (n - a - b + k1)))
                m += p0 * (k1 / n) * math.log((k1 * n) / (a * b), 2)
                k0 = k1
    fi_value = fraction_of_information_general(df, lhs, rhs)

    bias_estimator = m / (-1.0 * ((y_counts / n) * np.log2(y_counts / n)).sum())
    return fi_value - bias_estimator



def reliable_fraction_of_information_plus_general(
    df: pd.DataFrame,  lhs: List[Any], rhs: List[Any]
) -> float:
    """This measure is RFI redefined by us to result in a score in the range [0;1]."""
    return max(0.0, reliable_fraction_of_information_general(df, lhs, rhs))

# helper function
def batched(iterable, n):
    """Batch data into tuples of length n. The last batch may be shorter.
    Taken from https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):

        yield batch

def smoothed_fraction_of_information_general(
    df: pd.DataFrame, lhs: List[Any], rhs: List[Any], alpha: float = 0.5
) -> float:
    """This measures is smoothed mutual information as defined by [Pennerath, Mandros & Vreeken, 2020](https://doi.org/10.1145/3394486.3403178)."""
    r_size = df.shape[0]
    domX_size = df.loc[:, lhs].nunique()
    domY_size = df.loc[:, rhs].nunique()
    xy_counts = df.loc[:, lhs+rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    shannonYX_sum = 0.0
    for batch in batched(
        itertools.product(df.loc[:, lhs].unique(), df.loc[:, rhs].unique()), 10_000_000
    ):
        counts = pd.DataFrame(
            batch,
            columns=[lhs, rhs],
        )
        counts = counts.merge(xy_counts, on=[lhs, rhs], how="left")
        counts = counts.merge(x_counts, on=lhs, how="left")
        counts = counts.fillna(0.0)
        smoothedX = (counts["x_count"] + domY_size * alpha) / (
            r_size + domX_size * domY_size * alpha
        )
        smoothedYX = (counts["xy_count"] + alpha) / (
            r_size + domX_size * domY_size * alpha
        )
        shannonYX_sum += (smoothedYX * np.log2(smoothedYX / smoothedX)).sum()
    smoothed_shannonYX = -1.0 * shannonYX_sum
    y_counts = df.loc[:, rhs].value_counts().reset_index()
    y_counts.columns = [rhs, "y_count"]
    smoothedY = (y_counts["y_count"] + domX_size * alpha) / (
        r_size + domX_size * domY_size * alpha
    )
    smoothed_shannonY = -1.0 * (smoothedY * np.log2(smoothedY)).sum()
    return (smoothed_shannonY - smoothed_shannonYX) / smoothed_shannonY


def pdep_self_general(df: pd.DataFrame, y: List[Any]) -> float:
    """This measure is pdep(Y) as defined by [Piatetsky-Shapiro & Matheus, 1993](https://www.aaai.org/Library/Workshops/1993/ws93-02-015.php)."""
    return (df.loc[:, y].value_counts() / df.shape[0]).pow(2).sum()


def pdep_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is pdep as defined by [Piatetsky-Shapiro & Matheus, 1993](https://www.aaai.org/Library/Workshops/1993/ws93-02-015.php)."""
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)

    return (1 / df.shape[0]) * (counts["xy_count"].pow(2) / counts["x_count"]).sum()


def tau_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is tau as defined by [Piatetsky-Shapiro & Matheus, 1993](https://www.aaai.org/Library/Workshops/1993/ws93-02-015.php)."""
    pdepXY = pdep_general(df, lhs, rhs)
    pdepY = pdep_self_general(df, rhs)

    return (pdepXY - pdepY) / (1 - pdepY)


def mu_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is mu as defined by [Piatetsky-Shapiro & Matheus, 1993](https://www.aaai.org/Library/Workshops/1993/ws93-02-015.php)."""
    pdepXY = pdep_general(df, lhs, rhs)
    pdepY = pdep_self_general(df, rhs)
    r_size = df.shape[0]
    domX_size = df.loc[:, lhs].nunique()

    return 1.0 - ((1 - pdepXY) / (1 - pdepY)) * ((r_size - 1) / (r_size - domX_size)).values[0]


def mu_plus_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure is mu redefined by us to result in a score in the range [0;1]."""
    return max(0.0, mu_general(df, lhs, rhs))


measures_dict = {
    'rho': rho_general,
    'g1': g1_general,
    'g1_prime': g1_prime_general,
    'shannon_g1': shannon_g1_general,
    'shannon_g1_plus': shannon_g1_plus_general,
    'g2': g2_general,
    'g3': g3_general,
    'g3_prime': g3_prime_general,
    'fraction_of_information': fraction_of_information_general,
    'reliable_fraction_of_information': reliable_fraction_of_information_general,
    'pdep': pdep_general,
    'tau': tau_general,
    'mu': mu_general,
    'mu_plus' :mu_plus_general
}