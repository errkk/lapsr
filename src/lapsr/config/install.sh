#!/bin/sh

echo 'Copying upstart configs'
sudo cp /home/pi/lapsr/src/lapsr/config/upstart_loop.conf /etc/init/lapsr_loop.conf
sudo cp /home/pi/lapsr/src/lapsr/config/upstart_gunicorn.conf /etc/init/lapsr_gunicorn.conf
echo 'Run $ sudo start lapsr_gunicorn / lapsr_loop'
