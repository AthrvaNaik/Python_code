from pytube import YouTube

link=input()
yt1=YouTube(link)
videos=yt1.streams.all()
