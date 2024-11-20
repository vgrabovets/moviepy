from moviepy import VideoFileClip
from moviepy import vfx, afx

myclip = VideoFileClip("example.mp4")
myclip = myclip.with_effects(
    [vfx.Resize(width=460)]
)  # resize clip to be 460px in width, keeping aspect ratio

# fx method return a copy of the clip, so we can easily chain them
myclip = myclip.with_effects(
    [vfx.MultiplySpeed(2), afx.MultiplyVolume(0.5)]
)  # double the speed and half the audio volume

# because effects are added to Clip at runtime, you can also call them directly from your clip as methods
myclip = myclip.with_effects([vfx.MultiplyColor(0.5)])  # darken the clip
