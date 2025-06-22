import pandas as pd
from src.lib.helper.get_config_data import get_result_paths

def get_report_output(report_name, df):
    for output_file in get_result_paths(report_name):
        print(f"OUTPUT {output_file}")
        output_file = output_file.strip()
        if output_file.endswith('xlsx'):
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Results', index=False)
            yield output_file
        elif output_file.endswith('pptx'):
            #To implement
            print(f"pptx support not implemented.")
