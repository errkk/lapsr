#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lapsr.lib.TextStar import *
from subprocess import call
import time

from lapsr.common import FRAME_FILE, get_frame, get_space, FILENAME_FORMAT
from lapsr.config.settings import *

# Initialise display
display = TextStar('/dev/ttyAMA0')
display.sendCmd('Starting...')
display.setCurPos(1, 1)

# Pick up from last time
frame = get_frame()
loop_index = 0
clear_next = True

COMMAND = 'raspistill -o {out_path}/{frame} -w {w} -h {h} -t {t}'.format(
    out_path=OUT_PATH, w=W, h=H, t=200, frame=FILENAME_FORMAT)


def update_frame(frame):
    display.sendCmd('Frame {0}'.format(frame))
    display.setCurPos(2, 1)
    display.sendCmd(get_space())
    display.setCurPos(1, 1)
    with open(FRAME_FILE, 'w') as f:
        f.write(str(frame))


while True:
    if clear_next:
        display.sendCmd(TS_CLEAR)
        display.setCurPos(1, 1)
        clear_next = False

    call([COMMAND.format(frame=frame)], shell=True)

    if loop_index == 0 and frame > 0:
        display.sendCmd('Resuming {0}'.format(frame))
        clear_next = True

    update_frame(frame)
    frame += 1
    loop_index += 1

    time.sleep(INTERVAL)

