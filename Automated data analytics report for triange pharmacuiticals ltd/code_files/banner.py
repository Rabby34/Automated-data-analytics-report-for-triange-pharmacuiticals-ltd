from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz
import os

date = datetime.today() #variable date holds the current date, datetime library is used

timezone_select = pytz.timezone('Asia/Dhaka')
datetime_bd = datetime.now(timezone_select) # this holds the exact date like the date variable on top

time = datetime_bd.strftime("%I:%M %p") #this is the current time for adding in the time field
day = str(date.day) + '-' + str(datetime_bd.strftime("%b")) + '-' + str(date.year) #this is the current date

project_dir = os.path.abspath('..') #project path

img = Image.open(project_dir + r"/photos/banner.png")
image_draw = ImageDraw.Draw(img)

font_for_day_time = ImageFont.truetype(project_dir + r"/font/Poppins-Bold.ttf",16,encoding="unic")
font_for_title = ImageFont.truetype(project_dir + r"/font/Poppins-BoldItalic.ttf",21,encoding="unic")

image_draw.text((1075,42),day,(3,21,47),font=font_for_day_time)
image_draw.text((1095,82),time,(3,21,47),font=font_for_day_time)
image_draw.text((510,153),"Monthly Sales Report",(3,21,47),font=font_for_title)

img.save(project_dir + r"/photos/healthcare_banner.png")
# img.show()

print("banner got created")