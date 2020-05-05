#! /bin/bash
v4l2-ctl -i 2
      while [ 1 ]; do
	python /home/tsewang/Desktop/Stellacam/stellaimage/automating.py  # IERS- what time is it?
	sleep 10 
        ffmpeg -s ntsc -r 1 -f v4l2 -i /dev/video0 -y -t 1 ./latest%d.png  # capture frame from video stream
        cp ./latest1.png /home/tsewang/Desktop/Stellacam/stellaimage/Archive/$(date +%F_%H:%M:%S).png   
	python /home/tsewang/Desktop/Stellacam/stellaimage/imaging.py         # timestamp+correct  the image
	sleep 5
      done

