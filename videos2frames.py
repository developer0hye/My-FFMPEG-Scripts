import os
from pathlib import Path

root = "./"

def read_all_files_from_root(root, exts=(".png")):
    files_path = []
    
    for r, d, f in os.walk(root):
        for file in f:
            if file.lower().endswith(exts):
                files_path.append(os.path.join(r, file).replace(os.sep, '/'))
    return files_path

videos = read_all_files_from_root(root=root, exts=(".mp4"))

for video in videos:
    video_name = Path(video).resolve().stem
    
    if not os.path.isdir(video_name):
        os.mkdir(video_name)

    os.system("ffmpeg -i " + '"' + video + '"' + " -qscale:v 3 -filter:v fps=1 " + video_name + "/" + video_name + "_%05d.jpg")
print(videos)
