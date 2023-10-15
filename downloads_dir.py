import os
import sys

def get_downloads_dir():
    operation_system = sys.platform
    if operation_system.startswith('win'):
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif operation_system == 'darwin':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif operation_system.startswith('linux'):
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        return None

