import pandas as pd
import numpy as np

#  1. Perfect FD
def generate_perfect_fd_case(n=100):
    return pd.DataFrame({
        "A": [f"a{i}" for i in range(n)],
        "B": [f"b{i}" for i in range(n)],
    })

#  2. Low Support FD
def generate_low_support_fd_case(n=5):
    return pd.DataFrame({
        "A": [f"a{i}" for i in range(n)],
        "B": [f"b{i}" for i in range(n)],
    })

#  3. Single Violation
def generate_single_violation_case(n=100):
    df = pd.DataFrame({
        "A": ["x"] * n,
        "B": ["y"] * n,
    })
    df.loc[n - 1, "B"] = "z"  # break FD in one row
    return df

#  4. Frequent Violations
def generate_frequent_violations_case(n=100):
    return pd.DataFrame({
        "A": ["x"] * n,
        "B": ["y"] * (n // 2) + ["z"] * (n // 2),
    })

#  5. Dominant Clean Mapping
def generate_dominant_clean_mapping_case(n=100):
    clean_rows = pd.DataFrame({
        "A": ["x"] * (n - 10),
        "B": ["y"] * (n - 10),
    })
    violating_rows = pd.DataFrame({
        "A": [f"v{i}" for i in range(10)],
        "B": [f"d{i}" for i in range(10)],
    })
    return pd.concat([clean_rows, violating_rows], ignore_index=True)

#  6. High Cardinality RHS
def generate_high_cardinality_rhs_case(n=100):
    return pd.DataFrame({
        "A": [f"x{i % 10}" for i in range(n)],
        "B": [f"unique{i}" for i in range(n)],
    })

#  7. Low Entropy RHS
def generate_low_entropy_rhs_case(n=100):
    return pd.DataFrame({
        "A": [f"a{i}" for i in range(n)],
        "B": ["common"] * (n - 1) + ["rare"],
    })

#  8. Rare Severe Violation
def generate_rare_severe_violation_case(n=100):
    clean_rows = pd.DataFrame({
        "A": [f"a{i}" for i in range(n - 10)],
        "B": [f"b{i}" for i in range(n - 10)],
    })
    violator_rows = pd.DataFrame({
        "A": ["x"] * 10,
        "B": [f"v{i}" for i in range(10)],
    })
    return pd.concat([clean_rows, violator_rows], ignore_index=True)

#  9. Random Dependency (no FD)
def generate_random_dependency_case(n=100):
    return pd.DataFrame({
        "A": np.random.choice(range(1000), size=n),
        "B": np.random.choice(range(1000), size=n),
    })
    
# 10. Overcounting Duplicates
def generate_overcounting_duplicates_case(n=100):
    return pd.DataFrame({
        "A": ["a"] * (n // 2) + ["b"] * (n // 2),
        "B": ["x"] * (n // 2) + ["y"] * (n // 2),
    })

# 11. Cardinality Instability
def generate_cardinality_instability_case(n=100):
    return pd.DataFrame({
        "A": [f"a{i % 5}" for i in range(n)],
        "B": [f"b{i}" for i in range(n)],
    })

# 12. Overcorrecting Negative
def generate_overcorrecting_negative_case(n=100):
    return pd.DataFrame({
        "A": ["a"] * n,
        "B": ["b"] * (n - 1) + ["c"],
    })

# 13. Rare Categories
def generate_rare_categories_case(n=100):
    return pd.DataFrame({
        "A": [f"a{i}" for i in range(n)],
        "B": ["x"] * 95 + [f"y{i}" for i in range(5)],
    })


#  Wrap into dictionary
test_cases = {
    "perfect_fd": {
        "generator": generate_perfect_fd_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "low_support_fd": {
        "generator": generate_low_support_fd_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "single_violation": {
        "generator": generate_single_violation_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "frequent_violations": {
        "generator": generate_frequent_violations_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "dominant_clean_mapping": {
        "generator": generate_dominant_clean_mapping_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "high_cardinality_rhs": {
        "generator": generate_high_cardinality_rhs_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "low_entropy_rhs": {
        "generator": generate_low_entropy_rhs_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "rare_severe_violation": {
        "generator": generate_rare_severe_violation_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "random_dependency": {
        "generator": generate_random_dependency_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
        "overcounting_duplicates": {
        "generator": generate_overcounting_duplicates_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "cardinality_instability": {
        "generator": generate_cardinality_instability_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "overcorrecting_negative": {
        "generator": generate_overcorrecting_negative_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
    "rare_categories": {
        "generator": generate_rare_categories_case,
        "lhs": ["A"],
        "rhs": ["B"],
    },
}