import os
from subprocess import check_output

from lapsr.config.settings import OUT_PATH


APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
FRAME_FILE = os.path.join(APP_ROUTE, 'tmp', 'frame.txt')
FILENAME_FORMAT = '{frame:06d}.jpg'


def get_frame():
    try:
        with open(FRAME_FILE, 'r') as f:
            return int(f.read())
    except:
        return 0


def get_space():
    output = check_output(['du', OUT_PATH])
    lines = output.split('\n')
    last_line = lines[-2]
    bytes_used = int(last_line.split('\t')[0])
    MB = bytes_used / 1000.0
    return '{0:.3f} MB'.format(MB)
