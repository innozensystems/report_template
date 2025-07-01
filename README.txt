To create a new report with the name new_report, do the following

export PYTHONPATH=<path to project root>
bash ./create_new_report.sh new_report

Modify
report_config/new_report.yaml
sql/new_report.sql

then run
python3 ./src/new_report/new_report.py

output in

output/new_report.xlsx



