import re

def parse_file(input_file):
    column_mapping = {}
    results = []
    with open(input_file, 'r') as f:
        in_column_section = False
        in_results_section = False

        for line in f:
            # Detect the start of sections
            if line.strip() == "# COLUMN":
                in_column_section = True
                in_results_section = False
                continue
            elif line.strip() == "# RESULTS":
                in_column_section = False
                in_results_section = True
                continue
            elif line.strip().startswith("#"):
                in_column_section = False
                in_results_section = False
                continue

            # Process each section
            if in_column_section and line.strip():
                # Parse column mappings
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    col_number = int(parts[1].strip())
                    col_name = parts[0].strip().split('.')[1]
                    column_mapping[col_number] = col_name
            elif in_results_section and line.strip():
                # Collect results
                results.append(line.strip())

    return column_mapping, results

def translate_results(results, column_mapping):
    translated_results = []
    for line in results:
        cols, target = line.split("->")
        cols = cols.split(",")
        if(all([x for x in cols])): # some hyfd doesnt have lhs?
            translated_cols = [column_mapping.get(int(col.strip()), col.strip()) for col in cols]
            translated_target = column_mapping.get(int(target.strip()), target.strip())
            
            translated_results.append(f"{', '.join(translated_cols)} -> {translated_target}")
    
    return translated_results



if __name__ == '__main__':
    
    # Input and output file paths
    input_file = 'hyfd_adult_sample_10000'
    output_file = 'output.txt'
    
    column_mapping, results = parse_file(input_file)
    
    translated_results = translate_results(results, column_mapping)
    
    with open(output_file, 'w') as f:
        for result in translated_results:
            f.write(result + '\n')
    
    print(f"Results saved to {output_file}")
