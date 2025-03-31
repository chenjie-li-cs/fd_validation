# Functional Dependency (FD) Benchmark

This benchmark is designed to evaluate the effectiveness of functional dependency (FD) generation algorithms using various measures and a diverse collection of datasets.

## 📌 Supported Measures
Currently, we support the measures outlined in the paper:
> **"Measuring Approximate Functional Dependencies: A Comparative Study"**.

Note: We only evaluate FDs where both the Left-Hand Side (LHS) and Right-Hand Side (RHS) are present. **Key attributes (where LHS is empty) are not supported.**

---

## 🔧 How to Use

There are two ways to run the evaluation:

### 1️⃣ **Dataset Setup**
- No matter the source of the FDs (HyFD-generated or handwritten), you **must** create a dataset folder under `dataset/`.
- Example: If your dataset is named **my_dataset**, create the folder:
  ```
  dataset/my_dataset/
  ```

### 2️⃣ **Using Handwritten FDs**
- The FDs must follow the format:
  ```
  [LHS] -> [RHS]
  ```
  - Example:
    ```
    A -> B
    A, C -> D
    ```

### 3️⃣ **Using FDs Generated from HyFD**
- We support **raw** FD files output from **HyFD**, part of the [Metanome project](https://github.com/HPI-Information-Systems/Metanome).
- The output format from HyFD can be used directly.

### 4️⃣ **Other FD Sources**
- If your FDs come from another source, **convert** them into the **handwritten FD format** (as described in step 2).


## 🚀 Running the Benchmark
To run the evaluation, follow these steps:

1. Place your dataset and FD files inside `dataset/your_dataset/`.
2. Ensure the FDs are in the correct format (either handwritten or HyFD output).
3. Open and execute **[EvaluateFDsWithMeasures.ipynb](EvaluateFDsWithMeasures.ipynb)**, which serves as the main entry point for evaluating FDs.

---



# TODOs

1. add some descriptions to each fd
  a. "this fd requires further dmain expert verification"
  b. given a dataset without FDs, estimate what kinds of fds are more likely to appear and need what kind of verification process (data dependent verification process?)
  c. write down the exact procedure we follow:
    a) data collection
    b) source of fds
    c) classification of fds (ideas including: 
      - generate a summary for each fd about its evaluation results on exsiting FD measures
        i) "fd X->Y performs well in shannon-entropy based measures but not logical-entropy based measures"
        ii) "fd X->Y is a valid measure according to metric A, but lacks statistical significance based on hypothesis testing with significance level \alpha=blah"

March 17th
  a. "this fd requires further dmain expert verification"
  b. Estimate before we see FDs? given a dataset without FDs, estimate what kinds of fds are more likely to appear and need what verification process would likely be needed (data dependent verification process?)
  c. write down the exact procedure we follow:
    a) data collection
    b) source of fds
    c) classification of fds, ideas including: 
      - generate a summary for each fd about its evaluation results on exsiting FD measures
        i) "fd X->Y performs well in shannon-entropy based measures but not logical-entropy based measures"
        ii) "fd X->Y is a valid measure according to metric A, but lacks statistical significance based on hypothesis testing with significance level \alpha=blah"
      - cache some results for reuse in calculation of some measures (like cooccurence rate between X and Y)

manually add some semantically meaningful fds + negative examples too 
also add a file under each dataset about the rationale that why certain FDs hold/ not hold


