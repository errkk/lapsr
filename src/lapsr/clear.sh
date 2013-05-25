#!/bin/sh

echo 'Clearing Frames'
sudo stop lapsr_loop
sudo rm -f /data/*
sudo rm -f tmp/frame.txt
sudo start lapsr_loop
