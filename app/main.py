import pandas as pd

path = "/Users/aldmikon/Desktop/Python_road/Projects/medical_examination_data_analysis/initial_data/medical_examination.csv"
try:
    df = pd.read_csv(path)
    print(df.info())
    #filtered_df = df[df["cholesterol"] > 1]

    df["health_index"] = df["cholesterol"] + df["smoke"] + df["gluc"] + df["alco"] +df["smoke"] - df["active"] - df["cardio"]

    print(df.loc[df["health_index"] >= 3,["id","health_index"]])
except Exception as e:
    print(f"An error occurred - {e}")




