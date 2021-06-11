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

[link](https://superuser.com/questions/1389019/ffmpeg-how-to-extract-frames-of-a-video-at-a-certain-time-frame?noredirect=1&lq=1)

Use -ss and -to.

```
ffmpeg -ss hh:mm:ss -to hh:mm:ss -i video.mp4 out%05d.png
```

### Example
```
ffmpeg -ss 00:05:30 -to 00:42:30 -i video.mp4 out%05d.png
```

## Extract 1 screenshot for a video with ffmpeg at a given time?

[link](https://stackoverflow.com/questions/27568254/how-to-extract-1-screenshot-for-a-video-with-ffmpeg-at-a-given-time)

Use the -ss and -vframes option:

- For JPEG output use -q:v to control output quality. Full range is a linear scale of 1-31 where a lower value results in a higher quality. 2-5 is a good range to try.

- The select filter provides an alternative method for more complex needs such as selecting only certain frame types, or 1 per 100, etc.

- Placing -ss before the input will be faster. See FFmpeg Wiki: Seeking and this excerpt from the ffmpeg cli tool documentation:

```
ffmpeg -ss hh:mm:ss -i input -vframes 1 -q:v 2 output.jpg
```

### Example
```
ffmpeg -ss 01:23:45 -i input -vframes 1 -q:v 2 output.jpg
```


## Cutting the videos based on start and end time using ffmpeg

[link](https://stackoverflow.com/questions/18444194/cutting-the-videos-based-on-start-and-end-time-using-ffmpeg)

### Example

00:00:03 ~ 00:00:11 
```
ffmpeg  -ss 00:00:03 -t 00:00:08 -i movie.mp4 -async 1 cut.mp4
```

00:00:03 ~ 00:00:08 
```
ffmpeg -ss 00:00:03 -to 00:00:08 -i movie.mp4 -async 1 cut.mp4
```

