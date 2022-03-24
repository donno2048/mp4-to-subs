# mp4-to-subs

Turn mp4 input into subtitles compatible for youtube.

There is also a unicode-art version (not captions) with high resolution [here](https://github.com/donno2048/mp4-to-unicode)

## Demo

https://www.youtube.com/watch?v=o9eNY1_9mis

There is also a unicode-art version (not captions) with high resolution [here](https://github.com/donno2048/mp4-to-unicode)


## Usage

Run `python3 main.py > badapple.srt`

(Use another file with the name _video.mp4_ to convert it, you can use another output name too (other then _badapple_))

## Install dependencies

`pip3 install opencv-python Pillow`

(on Linux you may need to run `sudo apt-get install ffmpeg libsm6 libxext6 -y` to use `opencv`)

There is also [a branch compatible with youtube](https://github.com/donno2048/mp4-to-subs/tree/youtube) and a [demo](https://www.youtube.com/watch?v=o9eNY1_9mis)

There is also [a branch compatible with vtt for youtube](https://github.com/donno2048/mp4-to-subs/tree/vtt) with higher resolution and a [demo](https://www.youtube.com/watch?v=V6jGTFwRf00)
