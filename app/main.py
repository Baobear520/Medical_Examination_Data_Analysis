from datetime import date
from os import PathLike

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

#clean ap_lo [30,120]
#clean ap_hi [220, 70]
#clean height [100, 230]
#adjust sex int -> M, F
#adjust age days-> years



def open_csv(path: str | PathLike) -> DataFrame | None:
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"An error occurred - {e}")



def rename_columns(df: DataFrame| None) -> DataFrame:
    return df.rename(
        columns={
            "api_hi": "bp_syst",
            "api_lo": "bp_diast"
        }
    )

def redefining_data(df: DataFrame| None) -> DataFrame:
    if df is None:
        return pd.DataFrame()  # Handle the None case gracefully.

    # Map 'sex' values: 1 -> 'M', 2 -> 'F'

    df.loc[:, "sex"] = df.loc[:, "sex"].astype(str).map({1: "M", 2: "F"})
    #df["sex"] = df["sex"].map({1: "M", 2: "F"})
    # Convert 'age' from days to years
    #df["age"] = df["age"].apply(lambda x: x // 365)
    df.loc[:, "age"] = df.loc[:, "age"].apply(lambda x: x // 365)

    return df


def normalize_data(df: DataFrame) -> DataFrame | None:

    return df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) &
        (df['ap_lo'] <= df['ap_hi'])
        ]


def save_to_csv(source: DataFrame | None, path_to_file: PathLike | str) -> None:
    try:
        source.to_csv(path_to_file,index=False)
        print("OK")
    except Exception as e:
        print(f"An error occurred - {e}")


def main():
    base_path = "/Users/aldmikon/Desktop/Python_road/Projects/medical_examination_data_analysis/"
    initial_file_name = "medical_examination.csv"
    path_to_initial_data = base_path + "initial_data/" + initial_file_name
    result_data_file_name = "filtered_data.csv"
    path_to_result_data = base_path + "result_data/" + result_data_file_name

    df = open_csv(path_to_initial_data)
    df_normalized = normalize_data(df)
    df_redefined = redefining_data(df_normalized)
    df = rename_columns(df_redefined)
    save_to_csv(df,path_to_result_data)

if __name__ == "__main__":
    main()