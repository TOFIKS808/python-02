# pylint: skip-file
""" add src path to avoid problems with importing modules by modules in tests """
import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)
