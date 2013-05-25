import os
from subprocess import check_output


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
    output = check_output(['du', '/data'])
    bytes_used = int(output.split('\t')[0])
    MB = bytes_used / 1000 / 1000.0
    return '{0:.3f} MB'.format(MB)
