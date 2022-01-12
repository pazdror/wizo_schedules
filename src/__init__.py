import sys
from pathlib import Path

if sys.platform == 'win32':
    dlls_path = Path(__file__).parents[1]/'dlls'
    import os
    os.add_dll_directory(str(dlls_path))
    os.environ['FONTCONFIG_FILE'] = str(dlls_path/'fonts.conf')
