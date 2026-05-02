import pandas as pd
data = {
    "calories": [420, 380, 390, 395, 400],
    "duration": [50, 40, 45, 50, 65]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3", "day4", "day5"])
print(df)