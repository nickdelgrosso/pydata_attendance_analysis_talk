import os
from pathlib import Path
from glob import glob

def task_get_data():
    return {
        'actions': ['python get_data.py'],
        'targets': ['data/attendance.csv'],
    }

def task_plot_attendance():
    return {
        'actions': ['python plot_data.py'],
        'file_dep': ['data/attendance.csv'],
        'targets': ['figures/attendance.png'],
    }

def task_export_notebooks():
    for notebook in glob('*.ipynb'):
        yield {
        'name': 'export notebook' + notebook,
        'actions': ['jupyter nbconvert --to html ' + notebook],
        'file_dep': [notebook],
        'targets': [Path(notebook).stem + '.html'],
        }
        