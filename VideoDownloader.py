#!/usr/bin/env python3

#Importing Youtube from pytube library
from pytube import YouTube

def Download(link):
    youtubeObject  =YouTube(link)
    
#Setting the video to be downloaded in low resolution
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        
 #Downloading the video
        youtubeObject.download()
    except:
        print('An error has occured')
    print('Download is completed successfully')
    
 #The user will input the video link
link = input("Put the link of the video here : ")

#And then it will be downloaded and be saved in the same path where the user run the script
Download(link)
