from PIL.Image import open as imopen
from sys import argv
from datetime import timedelta
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
from numpy import array
SPACES = False # wheter to use spaces or not
file = open(argv[1], "w", encoding='utf8')
def I2T(File):
	im = imopen(File)
	w, h = im.size
	data = list(im.getdata())
	crop = lambda x: [255 if i > 255 else 0 if i < 0 else i for i in x]
	for y in range(h):
		for x in range(w):
			oldpixel = array(data[x + y * w])
			newpixel = array(list(map(lambda i: 255 if i > 127 else 0, oldpixel)))
			data[x + y * w] = newpixel
			quant_error = oldpixel - newpixel
			if x + 1 < w: data[x + 1 + y * w] = crop(data[x + 1 + y * w] + 7 * quant_error / 16)
			if x - 1 >= 0 and y + 1 < h: data[x - 1 + (y + 1) * w] = crop(data[x - 1 + (y + 1) * w] + 3 * quant_error / 16)
			if y + 1 < h: data[x + (y + 1) * w] = crop(data[x + (y + 1) * w] + 5 * quant_error / 16)
			if x + 1 < w and y + 1 < h: data[x + 1 + (y + 1) * w] = crop(data[x + 1 + (y + 1) * w] + 1 * quant_error / 16)
	black_and_white = []
	for y in range(h):
		for x in range(w):
			black_and_white.append(0.3 * data[x + y * w][0] + 0.586 * data[x + y * w][1] + 0.114 * data[x + y * w][2] < 127)
	for y in range(h // 3):
		for x in range(w // 2):
			file.write(chr(0x2800 + max(sum(map(lambda i: sum(map(lambda j: black_and_white[w * (i + 3 * y) + 2 * x + j], [0, 1])), [0, 1, 2])), not SPACES)))
		file.write("\n")
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
index = 0
while success:
	index += 1
	file.write(str(index) + "\n" + (str(timedelta(milliseconds = index * 100))[:11] + " --> " + str(timedelta(milliseconds = (index + 1) * 100))[:11]).replace('.', ',') + "\n")
	I2T(BytesIO(imencode(".jpg", resize(image, (42, 42), interpolation = 3))[1]))
	file.write("\n")
	vidcap.read()
	vidcap.read()
	success, image = vidcap.read()
file.close()