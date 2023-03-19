# mjpeg_stream_webcam with receier.py
meska/mjpeg_stream_webcam https://github.com/meska/mjpeg_stream_webcam に、受信機能を持たせた。

# 実行方法
- Terminal1
`python3 mjpegsw.py --camera 0 --port 5001 --ipaddress 0.0.0.0`

- Terminal2
`python3 receiver.py`

# mjpeg_stream_webcam
Webcam Streamer for Octoprint


I made this script for streaming an usb webcam to mjpeg suitable for OctoPrint on a mac, but it will probably work on
linux and windows too.

Tested on python 3.7

Installation:

* install homebrew from https://brew.sh/
* from console run `brew install python` to get python 3.7
* `pip install virtualenv` to install virtualenv
* clone/download the repository on your drive
* cd on the folder and run 
```
virtualenv -p python3.7 .env
source .env/bin/activate
pip install -r requirements.txt
```
* run the script with `python mjpegsw.py`or `.env/bin/python mjpegsw.py`

optional params:
`python mjpegsw.py --camera 1 --port 5001 --ipaddress 0.0.0.0`


on octoprint you can use http://localhost:5001/cam.mjpg for stream url and http://localhost:5001/snap.jpg for snapshot url.

### MacOs Yosemite:
you need to use opencv-python==4.0.0.21
```
pip install -r requirements.yosemite.txt
```

### OpenCv Segmentation fault
sometimes opencv crashes, for this you can use `start.sh` script that loops until you block it with CTRL-C
