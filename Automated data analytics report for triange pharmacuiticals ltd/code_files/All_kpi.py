from functions import convert,percentage,convert_small_amount

import pyodbc as db
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os


connection_string = (
                     r'DRIVER={ODBC Driver 17 for SQL Server};'
                     r'SERVER=(local)\SQLEXPRESS01;'
                     r'DATABASE=healthcareDB;'
                     r'UID=sa;'
                     r'PWD=12345;'
                     r'Trusted_Connection=yes;'
                    )

connection = db.connect(connection_string)
cursor  = connection.cursor()

target_sales_df  = pd.read_sql_query("""select a.zonecode as zone_code,isnull(a.budget_value,0) as budget,isnull(b.sale_value,0) as sales,b.budget_month from
                                            (select * from hpl_budget
                                            where budget_month=9) as a
                                            join
                                            (select * from hpl_sales
                                            where budget_month=9) as b
                                            on a.zonecode=b.zonecode""",connection)

target_list = target_sales_df['budget'].values.tolist()
Sales_list = target_sales_df['sales'].values.tolist()


# total target calculation
total_target = sum(target_list)
Converted_target = convert(total_target) # check the convert function in functions.py file


# total sales calculation
total_sale = sum(Sales_list)
Converted_sales = convert(total_sale) # check the convert function in functions.py file


# sales achievement calculation
sales_achievement= percentage(total_sale,total_target)

product_target_return_df  = pd.read_sql_query("""select product_code, product_name, total_sales, total_return
                                                     from hpl_products""",connection)


#sergel sell value calculation
Sergel_sell_value = product_target_return_df[product_target_return_df['product_name']=='Sergel'].values.tolist()[0][2]
converted_Sergel_sell_value = convert(Sergel_sell_value)


# super-8 sell value calculation
Super8_sell_value = product_target_return_df[product_target_return_df['product_name']=='Denvar'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Ferisen'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Renovit'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Rocal-reef'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Aeron'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Clonatril'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Furotil'].values.tolist()[0][2] + product_target_return_df[product_target_return_df['product_name']=='Lyric'].values.tolist()[0][2]
converted_Super8_sell_value = convert_small_amount(Super8_sell_value)


# total return value calculation
return_list = product_target_return_df['total_return'].values.tolist()
total_return = sum(return_list)
converted_total_return = convert_small_amount(total_return)


# Trend calculation here

# Trend calculation here


# values got added in the template
project_dir = os.path.abspath('..') #project path

kpi_img = Image.open(project_dir + r"/photos/project_kpi.png")
kpi_image_draw = ImageDraw.Draw(kpi_img)

font_for_kpi_values = ImageFont.truetype(project_dir + r"/font/centurygothic.ttf",38,encoding="unic")
font_for_no_data = ImageFont.truetype(project_dir + r"/font/centurygothic.ttf",32,encoding="unic")

kpi_image_draw.text((42,80),Converted_target,(255,255,255),font=font_for_kpi_values)
kpi_image_draw.text((350,80),Converted_sales,(255,255,255),font=font_for_kpi_values)
kpi_image_draw.text((655,80),sales_achievement,(255,255,255),font=font_for_kpi_values)
kpi_image_draw.text((965,80),converted_total_return,(255,255,255),font=font_for_kpi_values)
kpi_image_draw.text((42,230),"No Data",(255,255,255),font=font_for_no_data) # currently No data available for this field
kpi_image_draw.text((350,230),"No Data",(255,255,255),font=font_for_no_data) # currently No data available for this field
kpi_image_draw.text((657,225),converted_Sergel_sell_value,(255,255,255),font=font_for_kpi_values)
kpi_image_draw.text((965,225),converted_Super8_sell_value,(255,255,255),font=font_for_kpi_values)

kpi_img.save(project_dir + r"/photos/healthcare_project_kpi.png")
# kpi_img.show()

print("Kpi pic got generated")