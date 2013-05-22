#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lapsr.lib.TextStar import *
from datetime import datetime
from subprocess import call
import time


display = TextStar('/dev/ttyAMA0')
display.sendCmd('Oh Hai! 123')
display.setCurPos(2)

FILENAME_FORMAT = '%Y-%m-%d--%H-%M-%S'
INTERVAL = 6
OUT_PATH = '/data'
frame = 0


while True:
    filename = datetime.now().strftime(FILENAME_FORMAT)
    call(["raspistill -o {0}/{1}.jpg".format(OUT_PATH, filename)],
         shell=True)
    frame += 1
    display.sendCmd('Frame {0}'.format(frame))
    display.setCurPos(2, 1)

    time.sleep(INTERVAL)

