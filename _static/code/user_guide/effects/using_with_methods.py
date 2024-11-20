from moviepy import VideoFileClip
from moviepy import vfx, afx

myclip = VideoFileClip("example.mp4")
myclip = myclip.with_end(5)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip
