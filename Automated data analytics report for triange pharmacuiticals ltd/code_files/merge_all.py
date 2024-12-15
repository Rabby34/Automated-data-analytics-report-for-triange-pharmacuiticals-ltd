from PIL import Image, ImageDraw, ImageFont,ImageFilter
import os

project_dir = os.path.abspath('..') #project path

final_banner = Image.open(project_dir+"/photos/healthcare_banner.png")
final_project_kpi = Image.open(project_dir+"/photos/healthcare_project_kpi.png")
zone_wise_target_sales_kpi = Image.open(project_dir+"/photos/zone_wise_budget_sales.png")
signature_info = Image.open(project_dir+"/photos/healthcare_signature.png")

imageSize = Image.new("RGB",(1250,1000),color='#0e2c4a')

imageSize.paste(final_banner,(0,0))
imageSize.paste(final_project_kpi,(0,200))
imageSize.paste(zone_wise_target_sales_kpi,(20,511))
imageSize.paste(signature_info,(0,911))


imageSize.save(project_dir+"/photos/merged_pic.png")

print("All pictures are merged")