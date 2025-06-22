import importlib

def dynamic_import(module_name, function_name, report_name):
    try:
        module_path = f"src.{report_name}.lib.{module_name}"
        imported_module = importlib.import_module(module_path)
    except (ModuleNotFoundError, AttributeError):
        module_path = f"src.lib.{module_name}"
        imported_module = importlib.import_module(module_path)
    get_module_output_function = getattr(imported_module, function_name)
    return get_module_output_function

def create_report(report_name):
    #SQL Results
    get_sql_output = dynamic_import('run_sql', 'get_sql_output', report_name)
    columns, results = get_sql_output(report_name)

    # DataFrame creation and manipulation
    get_df_output = dynamic_import('run_df', 'get_df_output', report_name)
    df = get_df_output(results, columns=columns)

    # Output the results
    get_report_output = dynamic_import('run_report', 'get_report_output', report_name)
    for output_file in get_report_output(report_name, df):
        print(f'Results have been written to {output_file}')
