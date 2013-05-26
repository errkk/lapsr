#/bin/sh

cd stills
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=640:480 -o ~/Desktop/tlcam.avi -mf type=jpeg:fps=14 mf://@stills.txt
