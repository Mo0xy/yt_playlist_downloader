import pytube
import os

path = os.path.join(os.path.expanduser('~'), 'Downloads')

link = input("Please enter playlist url: ")

yt = pytube.Playlist(link)
pls = yt.video_urls


vd = pytube.YouTube(link)
indx = vd.streams.index(vd.streams.first())
while(indx != vd.streams.index(vd.streams.last())): 
    vd = pytube.YouTube(pls[indx])
    stream = vd.streams.get_highest_resolution()
    stream.download(path)
    indx += 1

print('Download is complete')
