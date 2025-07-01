import os
from pathlib import Path
from src.lib.helper.load_yaml import load_yaml

abs_dir = os.path.dirname(os.path.abspath(__file__))

def get_db_config_path():
    return f'{abs_dir}/../../../db_config.yaml'

def get_report_config_path(report_name):
    return f'{abs_dir}/../../../report_config/{report_name}.yaml'

def _get_report_config(report_name):
    report_config_path = get_report_config_path(report_name)
    report_config = load_yaml(report_config_path)
    return report_config

def get_db_config():
    app_config = load_yaml(get_db_config_path())
    return app_config['database']

def get_sql_params(report_name):
    sql_config = _get_report_config(report_name)
    return sql_config['params']

def _get_output_str(output_file, report_name):
    if output_file.startswith('/'):
        return output_file
    else:
        report_config_path = get_report_config_path(report_name)
        path = Path(report_config_path)
        full_path = str(path.parent.parent / output_file)
        return full_path

def get_result_paths(report_name):
    report_config = _get_report_config(report_name)
    output_file = report_config['paths']['output_file']
    if isinstance(output_file, str):
        return [_get_output_str(output_file, report_name)]
    elif isinstance(output_file, list):
        results = []
        for file in output_file:
            results.append(_get_output_str(output_file, report_name))
        return results
