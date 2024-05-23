import matplotlib.animation as animation
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def show_images_as_video(image_path, fps, cmap):
  '''
  This mehtod gets a group of images and reproduces a video at the specified fps

  :param image_path: path where the frames are located
  :param fps: number of fps we want to display the video
  :param cmap: it says if image are grayscale or not

  '''
  fig, ax = plt.subplots()

  if cmap == 'gray':
      image_display = ax.imshow(image_path[0], cmap='gray')
  else:
      image_display = ax.imshow(image_path[0])

  interval = 1000 / fps
  progress_bar = tqdm(total=len(image_path), desc="Processing frames", unit="frame")

  def update(frame):
      image_display.set_array(image_path[frame])
      progress_bar.update(1)
      if frame == len(image_path) - 1:
          progress_bar.reset()

  ani = animation.FuncAnimation(fig, update, frames=len(image_path), interval=interval, repeat=True)
  plt.axis('off')
  plt.show()
  progress_bar.close()