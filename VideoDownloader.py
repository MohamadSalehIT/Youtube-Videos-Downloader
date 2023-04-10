#!/usr/buin/env python3
from pytube import YouTube
def Download(link):
    youtubeObject  =YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
    except:
        print('An error has occured')
    print('Download is completed successfully')
link = input("Put the link of the video here : ")
Download(link)
