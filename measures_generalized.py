from typing import List, Any
import pandas as pd
import numpy as np

def rho_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    lhs_rhs_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    lhs_rhs_counts.columns = lhs + rhs + ["lhs_rhs_count"]
    lhs_counts = df.loc[:, lhs].value_counts().reset_index()
    return lhs_counts.shape[0] / lhs_rhs_counts.shape[0]

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

def g_prime_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
    violating_tuple_pairs = (
        (counts["xy_count"]) * (counts["x_count"] - counts["xy_count"])
    ).sum()
    return violating_tuple_pairs / ((df.shape[0] ** 2) - (xy_counts["xy_count"].pow(2)).sum())

def shannon_g1_general(df: pd.DataFrame, lhs: List[Any], rhs: List[Any]) -> float:
    """This measure calculates 1 - H_R(Y|X), where H_R is the conditional Shannon entropy."""
    r_size = df.shape[0]
    xy_counts = df.loc[:, lhs + rhs].value_counts().reset_index()
    xy_counts.columns = lhs + rhs + ["xy_count"]
    x_counts = df.loc[:, lhs].value_counts().reset_index()
    x_counts.columns = lhs + ["x_count"]
    counts = xy_counts.merge(x_counts, on=lhs)
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
