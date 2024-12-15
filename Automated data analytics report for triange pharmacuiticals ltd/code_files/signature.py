from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz
import os

project_dir = os.path.abspath('..') #project path

img_signature = Image.open(project_dir + r"/photos/signature.png")
image_draw = ImageDraw.Draw(img_signature)

font_for_name = ImageFont.truetype(project_dir + r"/font/centurygothic.ttf",16,encoding="unic")
font_for_signature = ImageFont.truetype(project_dir + r"/font/Pacifico-Regular.ttf",30,encoding="unic")

image_draw.text((925,40),'Developed by: ',(255,255,255),font=font_for_name)
image_draw.text((1050,20),"Fazle Rabby",(255,255,255),font=font_for_signature)


img_signature.save(project_dir + r"/photos/healthcare_signature.png")
# img_signature.show()

print("signature got created")