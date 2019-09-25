# This is still WIP and has some limitations:
	- As a parameter script can accept videos folder only as relative path in the current dir

# For Windows

1. Enter powershell:
	$ <Win + R>
	$ powershell
	# Or you can just search for it in Start menu (if you are noob)
2. Make sure you have python installed:
	$ python
	# First line should be python version. Usually 3.x.x
3. Install OpenCV library for python:
	$ pip install opencv-python
	$ pip install opencv-contrib-python
4. Make sure you've installed OpenCV correctly:
	$ python
	>>> import cv2
	>>> cv2.__version__

# Steps 1-4 should be done only once

5. Copy the videos folder into root directory of the script
6. Run the script:
	$ python framer.py <videos_folder_name>
	# Example: python framer.py vid
7. Frames should be in the videos folder when process is finished
