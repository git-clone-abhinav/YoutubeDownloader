import time
import os
print("==============================================")
print('Checking for yt_dlp library ',end = "")
print("."*5,end = "")
print("")
time.sleep(1)
try:
    import yt_dlp
    print("yt_dlp library found")
except:
    import os
    os.popen("pip install yt-dlp")
    print("yt_dlp library installed")
finally:
    print("==============================================")
    import yt_dlp

url = input("Enter the URL of the video or playlist : ")
# url = "https://www.youtube.com/playlist?list=PLZ2ps__7DhBbLZ6RdNTIXvFdaMpvqagt0"
playlist_start = int(input("Start Download from : ")) 
# playlist_start = 1
playlist_end = int(input("Finish Download at : ")) 
# playlist_end = 2
print("Starting Download...")
f_str = f"yt-dlp {url} --playlist-start {playlist_start} --playlist-end {playlist_end} --format 22 --write-subs --sub-lang en --sub-format srt"
os.system('cmd /c {}'.format(f_str))