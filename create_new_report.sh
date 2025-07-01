#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Error: You must provide exactly one argument."
    echo "Usage: $0 <new_report_name>"
    exit 1
fi
report_name=${1}
cp sql/sql_template.yaml "sql/${report_name}.sql"
cp report_config/report_template.yaml "report_config/${report_name}.yaml"

sed -i '' -e "s|output_file: 'output/report_template.xlsx'|output_file: 'output/${report_name}.xlsx'|g" "report_config/${report_name}.yaml"

mkdir -p "src/${report_name}"
cp "src/report_template/report_template.py" "src/${report_name}/${report_name}.py"
