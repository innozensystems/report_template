import os
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

def get_result_paths(report_name):
    report_config = _get_report_config(report_name)
    return report_config['paths']['output_file'].split(',')
