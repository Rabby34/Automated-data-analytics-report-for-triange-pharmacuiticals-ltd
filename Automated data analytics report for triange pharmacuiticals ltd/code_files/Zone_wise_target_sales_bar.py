import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc as db
import sys

project_dir = os.path.abspath('..')

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


budget_sales_df = pd.read_sql_query("""select top 10 a.zonecode as zone_code,a.zonename as zone_name,isnull(a.budget_value,0) as budget,
                                            isnull(b.sale_value,0) as sales,b.budget_month from
                                            (select * from hpl_budget
                                            where budget_month=9) as a
                                            join
                                            (select * from hpl_sales
                                            where budget_month=9) as b
                                            on a.zonecode=b.zonecode
											order by budget desc
                                            """, connection)


Zone_name = budget_sales_df['zone_name'].tolist()
zone_budget = budget_sales_df['budget'].tolist()
zone_sales = budget_sales_df['sales'].tolist()


#it helps to make zone_budget smaller that helps in plotting
budget_array=[]
for budget_value in zone_budget:
    new_value=round(budget_value/100000,1)
    budget_array.append(new_value)

#it helps to make zone_sales smaller that helps in plotting
sales_array=[]
for sales_value in zone_sales:
    new_value2=round(sales_value/100000,1)
    sales_array.append(new_value2)

# helps to arrange multiple bars
barWidth = .3 #space between multiple bars
br1 = np.arange(len(zone_budget))
br2 = [x + barWidth for x in br1]

fig, ax = plt.subplots(figsize=(12.1, 4),facecolor='#0e2c4a') #it creates the size of the graph 1250*400


width = .25 # the width of the bars
rects2 = ax.bar(br1, budget_array,width=width, label='Budget',color='#65B556')
rects3 = ax.bar(br2, sales_array,width=width, label='Sales',color='#578961')
# line = ax.plot(Target, color='green', label='Target')


# plt.yticks([])
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
plt.xticks(rotation=0)
# ax.set_xticks(x)
ax.legend(fontsize=10,loc='upper right')
plt.xlabel('Zone', fontweight ='bold', fontsize = 13,color='#ffffff',labelpad=15)
plt.ylabel('budget & sales (in lakh)', fontweight ='bold', fontsize = 13,color='#ffffff',labelpad=15)
plt.xticks([r-.13 + barWidth for r in range(len(Zone_name))],
        Zone_name)
ax.set_xticklabels(Zone_name,color='black')
ax.tick_params(axis='y', colors='white', labelsize=10)
ax.tick_params(axis='x', colors='white', labelsize=10)
ax.set_facecolor("#0e2c4a")
plt.title("Top 10 Zone Wise Target & Sales",color='white', fontsize=15, rotation=0, fontweight='bold',pad=15)


# plt.text(x[0], Target[0]+1000, format(Target[0], ',')+'K',fontsize=9,color='green', fontweight='bold')

def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height,
                height,
                    ha='center', va='bottom',color='white', fontsize=8, rotation=0, fontweight='bold')

autolabel(rects2)
autolabel(rects3)

plt.rcParams['savefig.facecolor'] = '#0e2c4a'
#011936

fig.tight_layout()
# plt.show()
plt.savefig(project_dir+"/photos/zone_wise_budget_sales.png")
print("Zone wise target sales bar chart got created")
#plt.close()