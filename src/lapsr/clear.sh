#!/bin/sh

echo 'Stopping process'
sudo stop lapsr_loop
echo 'Clearing frames'
sudo rm -f /home/pi/mnt/*.jpg
echo 'Resetting frame count'
sudo rm -f tmp/frame.txt
echo 'To start again, run this:'
echo 'sudo start lapsr_loop'
