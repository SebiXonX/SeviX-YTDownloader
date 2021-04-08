import Updater
from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
import os
import subprocess
import time
import pyfiglet
import imgdownloader as mgd

while True:
    print("1) Film")
    print("2) Audio")
    print("4) Update")
    print("5) Exit")
    file = int(input("Selected: "))

    if file == 1:
        print("1) Videos")
        print("2) Playlists")
        file2 = int(input("Selected: "))
        
        if file2 == 1:
            url = input("URL: ")
            subprocess.call("cls", shell=True)
            _filename = YouTube(url).title
            # Downloading
            YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download(filename=_filename)
            time.sleep(1)
            
        elif file2 == 2:
            url = input("Playlist URL: ")
            subprocess.call("cls", shell=True)
            playlist = Playlist(url)
            for video_url in tqdm(playlist.video_urls):
                try:
                    _filename = YouTube(video_url).title
                    # Downloading
                    YouTube(video_url).streams.filter(progressive=True, file_extension='mp4').first().download(filename=_filename)
                    time.sleep(1)
                except:
                    print("Error: " + video_url)
                    
    elif file == 2:
        print("1) Videos")
        print("2) Playlists")
        file2 = int(input("Selected: "))
        
        if file2 == 1:
            url = input("URL: ")
            subprocess.call("cls", shell=True)
            _filename = YouTube(url).title
            # Downloading
            YouTube(url).streams.filter(only_audio=True).first().download(filename=_filename)
            time.sleep(1)
            # Converting
            mp4 = '"' + _filename + ".mp4" + '"'
            mp3 = '"' + _filename + ".mp3" + '"'
            ffmpeg = 'ffmpeg -i ' + mp4 + " " + mp3
            subprocess.call(ffmpeg, shell=True)
        elif file2 == 2:
            url = input("Playlist URL: ")
            subprocess.call("cls", shell=True)
            playlist = Playlist(url)
            for video_url in tqdm(playlist.video_urls):
                try:
                    _filename = YouTube(video_url).title
                    # Downloading
                    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=_filename)
                    time.sleep(1)
                except:
                    print("Error: " + video_url)
            for video_url in tqdm(playlist.video_urls):
                _filename = YouTube(video_url).title
                # Converting
                mp4 = '"' + _filename + ".mp4" + '"'
                mp3 = '"' + _filename + ".mp3" + '"'
                ffmpeg = 'ffmpeg -i ' + mp4 + " " + mp3
                subprocess.call(ffmpeg, shell=True)
    
    elif file == 4:
       Update.Search()
        
    elif file == 5:
        break;
        
    else:
       print("Bad!")
