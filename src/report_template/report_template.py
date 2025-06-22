import os
from src.lib.create_report import create_report

if __name__ == '__main__':
    base_name = os.path.splitext(os.path.basename(__file__))[0]
    create_report(base_name)
