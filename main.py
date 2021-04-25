try: from PIL.Image import open
except: from Image import open
from sys import stdout
from datetime import timedelta, datetime
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
def I2T(File):
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	for pixel in data:
		if field:
			if pixel > 127: stdout.write("⬛")
			else: stdout.write("⬜")
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: stdout.write("\n")
			field = not field
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
index = 0
dt0 = datetime(1, 1, 1)
print("WEBVTT")
while success:
	index += 1
	print()
	print((dt0 + timedelta(milliseconds = index * 200)).strftime("%M:%S.%f")[:9] + " --> " + (dt0 + timedelta(milliseconds = (index + 1) * 200)).strftime("%M:%S.%f")[:9] + " size:50%")
	I2T(BytesIO(imencode(".jpg", resize(image, (48, 64), interpolation = 3))[1]))
	[vidcap.read() for i in range(5)]
	success, image = vidcap.read()
