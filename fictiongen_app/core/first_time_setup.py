"""
Copy over example settings if this is the first run
"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dest_file_path = os.path.join(BASE_DIR, 'core' , 'local_settings.py')
example_file_path = os.path.join(BASE_DIR, 'core',  'local_settings.example')
exists = os.path.isfile(dest_file_path)
if not exists:
    shutil.copy(example_file_path, dest_file_path)