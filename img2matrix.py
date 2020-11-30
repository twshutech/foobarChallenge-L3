import numpy as np
from PIL import Image
import glob

def toStack():
  filenames = glob.glob('/b106d6c5ea639067c0f8310081a99288.png')
  print(filenames)
  images = [Image.open(fn).convert('L') for fn in filenames]
  data = np.dstack([np.array(im) for im in images])
  print(data)

toStack()
