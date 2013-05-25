#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template

from lapsr.common import get_frame, get_space, FILENAME_FORMAT


app = Flask(__name__)


@app.route("/")
def hello():
    frame = get_frame()
    data = {
        'frame': frame,
        'image': FILENAME_FORMAT.format(frame=frame),
        'IMAGES_URL': '/m/',
        'space': get_space()
    }
    return render_template('base.html', data=data)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=9000)
