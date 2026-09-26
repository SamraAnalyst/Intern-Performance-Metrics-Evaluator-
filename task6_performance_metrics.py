import pandas as pd
import numpy as np

print("---- Step 1: Ingesting Raw Performance Metric Streams ----")

raw_performances ={
    "Intern_Name": ["Samra", "Ahmed", "Sana", "Zain", "Ali"],
    "Completion_Time_(Days)": [12, 25, 14, 20, 27],
    "Project_Quality_(%)": [85, 60, 95, 75, 50],
    "Mentor_Feedback": [8, 6, 9, 5, 7]

}
df = pd.DataFrame(raw_performances)
print("\n Intial Intern Performance Matrix Table:")
print(df)

print("\n ---- Step 2: Running Evaluation Performance Analytics ---")
df["Performance_Index"] = np.round((df["Project_Quality_(%)"] * df["Mentor_Feedback"]) / df["Completion_Time_(Days)"], 2)

print("\n --- Step 3: Sorting Intern Ranking for Supervisor Report ---")
df_sorted = df.sort_values(by="Performance_Index", ascending=False)

print("\n Final Sorted Structural Performace Dashboard:")
print(df_sorted[["Intern_Name", "Performance_Index"]])
