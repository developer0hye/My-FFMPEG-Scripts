# MY-FFMPEG-Scripts

## Create a video from images
```
ffmpeg -i %05d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4
```

## Extract a good quality JPEG image from a video file

[link](https://stackoverflow.com/questions/10225403/how-can-i-extract-a-good-quality-jpeg-image-from-a-video-file-with-ffmpeg)

Use -qscale:v (or the alias -q:v) as an output option.

- Normal range for JPEG is 2-31 with 31 being the worst quality.
- The scale is linear with double the qscale being roughly half the bitrate.
- Recommend trying values of 2-5.
- You can use a value of 1 but you must add the -qmin 1 output option (because the default is -qmin 2).

```
ffmpeg -i input.mp4 -qscale:v 2 output_%03d.jpg
```

## Extract frames of a video at a certain time frame

Use -ss and -to.

```
ffmpeg -ss hh:mm:ss -to hh:mm:ss -i video.mp4 out%05d.png
```

### Example
```
ffmpeg -ss 00:05:30 -to 00:42:30 -i video.mp4 out%05d.png
```
