import os
import subprocess

path = '/mnt/sdb/plex/tvshows/90 Day Fiancé - Happily Ever After!/Season 4'
preset = 'General/Fast 720p30'

for video in os.listdir(path):
    if "1080p" in video:
        fullPath = os.path.join(path, video)
        subprocess.run(["HandBrakeCLI", "--preset=" + preset, "--input=" + fullPath, "--output=" + fullPath.replace('1080p.mkv','720p.m4v')])
