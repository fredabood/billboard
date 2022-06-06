# Databricks notebook source
import ast
from datetime import datetime
from pprint import pprint
import pandas as pd

# COMMAND ----------

charts = ast.literal_eval(open('charts.json','r').read())`

# COMMAND ----------

status = []
for chart in charts:
    for category in charts[chart]:
        if charts[chart][category] > 0:
            charts[chart][category] = pd.to_datetime(str(charts[chart][category]), format='%Y%m%d')
        else:
            charts[chart][category] = None
        
        status.append(dict(chart=chart, category=category, date=charts[chart][category]))

# COMMAND ----------

status = pd.DataFrame(status)

# COMMAND ----------

status.sort_values('date',ascending=False).to_csv('status.csv', index=False, encoding='utf-8')
