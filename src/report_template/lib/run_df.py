import pandas as pd

def get_df_output(results, columns):
    # DataFrame creation and manipulation
    print(f"Dataframe code specific to report...")
    df = pd.DataFrame(results, columns=columns)
    print(df)
    return df
