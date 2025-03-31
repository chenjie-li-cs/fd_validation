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




#  weakness diagnosis config dictionary
measure_diagnosis_config = {
    "rho": {
        "known_weakness_cases": {
            "low_support_fd": {
                "expected_diagnosis": {
                    "fraction_of_information": lambda s: s < 0.6,
                    "pdep": lambda s: s < 0.7,
                }
            },
            "frequent_violations": {
                "expected_diagnosis": {
                    "g3": lambda s: s < 0.7,
                    "g2": lambda s: s < 0.8,
                }
            },
        }
    },
    "g1": {
        "known_weakness_cases": {
            "single_violation": {
                "expected_diagnosis": {
                    "rho": lambda s: s < 1.0,
                    "g3": lambda s: s < 1.0,
                    "g2": lambda s: s < 1.0,
                }
            },
            "overcounting_duplicates": {
                "expected_diagnosis": {
                    "g1_prime": lambda s: s > 0.95,
                    "g3": lambda s: s > 0.95,
                }
            },
        }
    },
    "g3": {
        "known_weakness_cases": {
            "rare_severe_violation": {
                "expected_diagnosis": {
                    "g2": lambda s: s < 0.7,
                    "pdep": lambda s: s > 0.9,
                }
            }
        }
    },
    "g3_prime": {
    "known_weakness_cases": {
        "single_violation": {
            "expected_diagnosis": {
                "g2": lambda s: s > 0.9,
                "rho": lambda s: s < 1.0,
            }
        }
    }
    },
    "g2": {
        "known_weakness_cases": {
            "broad_sparse_violations": {
                "expected_diagnosis": {
                    "g3": lambda s: s < 0.8,
                    "fraction_of_information": lambda s: s < 0.7,
                }
            }
        }
    },
    "fraction_of_information": {
        "known_weakness_cases": {
            "high_cardinality_rhs": {
                "expected_diagnosis": {
                    "rho": lambda s: s < 0.9,
                    "pdep": lambda s: s < 0.9,
                    "g3": lambda s: s < 0.9,
                }
            },
            "low_entropy_rhs": {
                "expected_diagnosis": {
                    "reliable_fraction_of_information": lambda s: s < 0.4,
                    "g2": lambda s: s < 0.9,
                    "g3": lambda s: s < 0.9,
                }
            }
        }
    },
    "pdep": {
        "known_weakness_cases": {
            "dominant_clean_mapping": {
                "expected_diagnosis": {
                    "g3": lambda s: s < 0.9,
                    "rho": lambda s: s < 1.0,
                    "fraction_of_information": lambda s: s < 0.9,
                }
            }
        }
    },
    "mu": {
        "known_weakness_cases": {
            "cardinality_instability": {
                "expected_diagnosis": {
                    "pdep": lambda s: s > 0.5,
                }
            }
        }
    },
    "reliable_fraction_of_information": {
        "known_weakness_cases": {
            "overcorrecting_negative": {
                "expected_diagnosis": {
                    "fraction_of_information": lambda s: s > 0.0,
                }
            }
        }
    },
    "shannon_g1": {
        "known_weakness_cases": {
            "rare_categories": {
                "expected_diagnosis": {
                    "smoothed_fraction_of_information": lambda s: s > 0.4,
                    "g3": lambda s: s > 0.7,
                }
            }
        }
    },

    "shannon_g1_plus": {
    "known_weakness_cases": {
        "rare_categories": {
            "expected_diagnosis": {
                "smoothed_fraction_of_information": lambda s: s > 0.4,
                "g3": lambda s: s > 0.7,
            }
        }
    }
    },
    "g1": {
        "known_weakness_cases": {
            "overcounting_duplicates": {
                "expected_diagnosis": {
                    "g1_prime": lambda s: s > 0.95,
                    "g3": lambda s: s > 0.95,
                }
            }
        }
    },
    "g1_prime": {
    "known_weakness_cases": {
        "overcounting_duplicates": {
            "expected_diagnosis": {
                "g1": lambda s: s < 0.95,
                "g3": lambda s: s > 0.95,
            }
        }
      }
    },
    "reliable_fraction_of_information": {
        "known_weakness_cases": {
            "overcorrecting_negative": {
                "expected_diagnosis": {
                    "fraction_of_information": lambda s: s > 0.0,
                }
            }
        }
    },
    "tau": {
        "known_weakness_cases": {
            "random_dependency": {
                "expected_diagnosis": {
                    "rho": lambda s: s < 0.3,
                    "fraction_of_information": lambda s: s < 0.4,
                }
            }
        }
    },
    "smoothed_fraction_of_information": {
        "known_weakness_cases": {
            "rare_categories": {
                "expected_diagnosis": {
                    "g3": lambda s: s > 0.7,
                }
            }
        }
    },
    "g1_prime": {
        "known_weakness_cases": {
            "overcounting_duplicates": {
                "expected_diagnosis": {
                    "g1": lambda s: s < 0.95,
                    "g3": lambda s: s > 0.95,
                }
            }
        }
    },
    "shannon_g1_plus": {
        "known_weakness_cases": {
            "rare_categories": {
                "expected_diagnosis": {
                    "smoothed_fraction_of_information": lambda s: s > 0.4,
                    "g3": lambda s: s > 0.7,
                }
            }
        }
    },
    "g3_prime": {
        "known_weakness_cases": {
            "single_violation": {
                "expected_diagnosis": {
                    "g2": lambda s: s > 0.9,
                    "rho": lambda s: s < 1.0,
                }
            }
        }
    },
    "mu_plus": {
        "known_weakness_cases": {
            "cardinality_instability": {
                "expected_diagnosis": {
                    "pdep": lambda s: s > 0.5,
                    "mu": lambda s: s < 0.5,
                }
            }
        }
    }
}

def gen_summary_df(csv_file_dir, measures_dict, input_file_hyfd=None, input_handwritten_file=None):
    runtimes = {}
    
    if(input_file_hyfd):
        column_mapping, results = parse_file(input_file_hyfd)
        display(column_mapping)
        # print(len(column_mapping))
        translated_results = translate_results(results, column_mapping)
    elif(input_handwritten_file):
        with open(input_handwritten_file, 'r') as f:
            lines = f.readlines()
            translated_results = []
            for line in lines:
                cols, target = line.split("->")
                cols = cols.split(",")
                if(all([x for x in cols])): # some hyfd doesnt have lhs?
                    translated_cols = [col.strip() for col in cols]
                    translated_target = target.strip()
                    translated_results.append(f"{', '.join(translated_cols)} -> {translated_target}")

    print("translated_results:")
    print(translated_results)
    data_df = pd.read_csv(csv_file_dir)
    # cols = [x.strip().replace('-','_') for x in list(data_df)]
    # print(cols)
    print(data_df.head())
    # data_df.columns = cols
    res_dfs = []
    for k in measures_dict:
        start_time = time.time()
        print(f"working on {k}")
        df_from_measure = test_fd_with_a_measure(measure_dict=measures_dict, measure_name=k, cand_fds=translated_results, data_df=data_df)
        res_dfs.append(df_from_measure)
        end_time = time.time()
        runtimes[k] = end_time - start_time
    return res_dfs, runtimes, translated_results

def run_weakness_diagnostics(
    measure_diagnosis_config,
    fd_measures,
    test_cases
):
    records = []

    for measure_name, config in measure_diagnosis_config.items():
        known_cases = config["known_weakness_cases"]

        for case_name, case_info in known_cases.items():
            if case_name not in test_cases:
                continue

            test_case = test_cases[case_name]
            df = test_case["generator"]()
            lhs = test_case["lhs"]
            rhs = test_case["rhs"]
            
            base_score = fd_measures[measure_name](df, lhs, rhs)


            for diag_fn_name, condition in case_info["expected_diagnosis"].items():

                diag_score = fd_measures[diag_fn_name](df, lhs, rhs)
                passed = condition(diag_score)
                result = "WEAK" if passed else "ROBUST"

                records.append({
                    "measure": measure_name,
                    "test_case": case_name,
                    "base_score": round(base_score,1),
                    "diagnostic_fn": diag_fn_name,
                    "diagnostic_score": round(diag_score,1),
                    "result": result,
                })

    return pd.DataFrame.from_records(records)