from pytube import YouTube


link = input("Enter your link ")
v = YouTube(link)

s = v.streams.get_highest_resolution()
s.download()

