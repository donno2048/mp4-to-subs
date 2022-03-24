# mp4-to-subs

Turn mp4 input into braille subtitles compatible for youtube.

There is also a unicode-art version (not captions) with high resolution [here](https://github.com/donno2048/mp4-to-unicode)

## Demo

https://youtu.be/nYYAeVdEu8Q

## Usage

Run `python3 main.py badapple.srt`

(Use another file with the name _video.mp4_ to convert it, you can use another output name too (other then _badapple_))

## Install dependencies

`pip3 install opencv-python Pillow numpy`

(on Linux you may need to run `sudo apt-get install ffmpeg libsm6 libxext6 -y` to use `opencv`)
