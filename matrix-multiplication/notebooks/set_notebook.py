import os
import sys


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(THIS_DIR)

PROBLEM_STATEMENTS_DIR = os.path.join(PROJECT_DIR, "problem_statements")


def add_to_python_path():
    sys.path.insert(0, PROJECT_DIR)
