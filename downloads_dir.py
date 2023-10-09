import os
import sys

def get_downloads_dir():
    operation_system = sys.platform 
    if operation_system.startswith('win'):
        # Windows
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif operation_system == 'darwin':
        # macOS
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif operation_system.startswith('linux'):
        # Linux
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        # OS not supported
        return None

downloads_dir = get_downloads_dir()
