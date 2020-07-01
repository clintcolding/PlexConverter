import os
import subprocess

path = '<full path to folder>'
preset = 'General/Fast 720p30'

for video in os.listdir(path):
    if "1080p" in video:
        fullPath = os.path.join(path, video)
        subprocess.run(["HandBrakeCLI", "--preset=" + preset, "--input=" + fullPath, "--output=" + fullPath.replace('1080p.mkv','720p.m4v')])
