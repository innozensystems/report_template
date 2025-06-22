import pandas as pd

def get_df_output(results, columns):
    # DataFrame creation and manipulation
    df = pd.DataFrame(results, columns=columns)
    print(df)
    return df
