from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageFilter
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# запрос с сайта requests
url = 'https://blog.skillfactory.ru/programmist-v-sims-4/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
title = soup.find('h1')
title = title.text
print(title)

#  pilloW
image = Image.open('hands.jpg')
#обрезка
width, height = image.size
area = (0, 0, width / 2, height / 2)
crop_img = image.crop(area)
# фильтр
img = image.filter(ImageFilter.EMBOSS)
#img2 = Image.open("car.jpg")
#image.paste(img2, (50, 50))
#img1.save("pasted_picture.jpg")
#image.thumbnail(size)
#image.save('2car.jpg')
# формат png
try:
    image = Image.open("hands.jpg")
except IOError:
    print("Unable to load image")
    sys.exit(1)

image.save('hands.png', 'png')
image.show()

# matplotlib
series = pd.Series(3 * np.random.rand(4),
                   index=['a', 'b', 'c', 'd'], name='series')

series.plot.pie(figsize=(4, 4))
plt.show()