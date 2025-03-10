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

