import pandas as pd 

def test_fd_with_a_measure(measure_dict, measure_name, cand_fds, data_df):
    res = []
    for fd in cand_fds:
        # print(f"on {fd}, using measure {measure_name}")
        lhs, rhs = fd.split(' -> ')
        lhs = [x for x in lhs.split(', ')]
        rhs = [x for x in rhs.split(', ')]
        val = measure_dict[measure_name](df=data_df, lhs=lhs, rhs=rhs)
        # print(f"res = {val}\n")
        res.append({'measure':measure_name, 'fd':fd, 'val':val})
    return pd.DataFrame(res)
