try: from PIL.Image import open
except: from Image import open
from sys import stdout
from datetime import timedelta
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
while success:
	index += 1
	print(index)
	print((str(timedelta(milliseconds = index * 100 / 3))[:11] + " --> " + str(timedelta(milliseconds = (index + 1) * 100 / 3))[:11]).replace('.', ','))
	I2T(BytesIO(imencode(".jpg", resize(image, (24, 32), interpolation = 3))[1]))
	print()
	success, image = vidcap.read()
	
