import pandas as pd
from scipy.stats import chi2_contingency


def chi_square_test(df, x, y):
    contingency_table = pd.crosstab(df[x], df[y])
    res = chi2_contingency(contingency_table)
    # chi2, p, dof, expected = chi2_contingency(contingency_table)

    # result = {
    #     "Chi2 Statistic": chi2,
    #     "p-value": p,
    #     "Degrees of Freedom": dof,
    #     "Expected Frequencies": expected
    # }
    
    # if p < 0.05:
    #     conclusion = "Reject the null hypothesis: There is a functional dependency."
    # else:
    #     conclusion = "Fail to reject the null hypothesis: No functional dependency detected."

    
    return res, contingency_table