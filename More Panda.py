import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [14, 15, 14, 16],
    "Score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df)

high_scores = df[df["Score"] > 80]
print(high_scores)

sorted_df = df.sort_values(by="Score", ascending=False)
print(sorted_df)

df["Result"] = df["Score"].apply(lambda x: "Pass" if x >= 80 else "Fail")
print(df)

average_score = df["Score"].mean()
print(average_score)