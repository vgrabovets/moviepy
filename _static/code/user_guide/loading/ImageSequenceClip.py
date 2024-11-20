from moviepy import *

# A clip with a list of images showed for 1 second each
myclip = ImageSequenceClip(
    [
        "example_img_dir/image_0001.jpg",
        "example_img_dir/image_0002.jpg",
        "example_img_dir/image_0003.jpg",
    ],
    durations=[1, 1, 1],
)
print(
    "Clip duration: {}".format(myclip.duration)
)  # 3 images, 1 seconds each, duration = 3
print("Clip fps: {}".format(myclip.fps))  # 3 seconds, 3 images, fps is 3/3 = 1

# This time we will load all images in the dir, and instead of showing theme for X seconds, we will define FPS
myclip2 = ImageSequenceClip("./example_img_dir", fps=30)
print(
    "Clip duration: {}".format(myclip2.duration)
)  # fps = 30, so duration = nb images in dir / 30
print("Clip fps: {}".format(myclip2.fps))  # fps = 30

myclip.write_gif("result.gif")  # the gif will be 3 sec and 1 fps
myclip2.write_gif(
    "result2.gif"
)  # the gif will be 30 fps, duration will vary based on number of images in dir
