import os
import yaml
#import psycopg2
from pathlib import Path
import sqlite3
from src.lib.helper.load_yaml import load_yaml
from src.lib.helper.get_config_data import get_db_config, get_sql_params

abs_dir = os.path.dirname(os.path.abspath(__file__))

def read_sql_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def execute_sql_file(query, params, db_config):
    print(f"query={query} params={params} db_config={db_config}")
    try:
        file_name = Path(db_config['dbname']).name
        conn = sqlite3.connect(db_config['dbname'])
    except Exception:
        file_path = Path(__file__)
        abs_dir = file_path.resolve().parent.parent.parent
        print(f"-----{abs_dir}")
        file_path = abs_dir / file_name
        print(f"-----{file_path}")
        conn = sqlite3.connect(file_path)

    cur = conn.cursor()

    cur.execute(query, params)

    columns = [desc[0] for desc in cur.description]
    results = cur.fetchall()

    cur.close()
    conn.close()

    return columns, results

def get_sql_query_and_params(report_name):
    sql_file_path = f'{abs_dir}/../../sql/{report_name}.sql'
    sql_query = read_sql_file(sql_file_path)
    sql_params = list(get_sql_params(report_name).values())
    return sql_query, sql_params

def get_sql_output(report_name):
    db_config = get_db_config()
    sql_query, sql_params = get_sql_query_and_params(report_name)
    return execute_sql_file(sql_query, sql_params, db_config)
