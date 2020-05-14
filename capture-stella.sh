#! /bin/bash
v4l2-ctl -i 2
      while [ 1 ]; do
	python3 /home/iiap/Desktop/stellacam/automating.py  # IERS- what time is it?
	sleep 10 
        ffmpeg -s 650*490 -r 1 -f v4l2 -i /dev/video0 -y -t 1 ./latest%d.png  # capture frame from video stream
        cp ./latest1.png /home/iiap/Desktop/stellacam/Temp/$(date +%F_%H:%M:%S).png   
	python3 /home/iiap/Desktop/stellacam/imaging.py         # timestamp+correct  the image
	sudo cp ./tonight.png /opt/lampp/htdocs/IAO/sky/allskycamera
	sudo cp ./moon_motion.png /opt/lampp/htdocs/IAO/sky/allskycamera
	sudo cp ./planets_motion.png /opt/lampp/htdocs/IAO/sky/allskycamera
	sleep 5
      done

