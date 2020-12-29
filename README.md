# MY-FFMPEG-Scripts

## Create a video from images
```
ffmpeg -i %05d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4
```
