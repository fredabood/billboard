# Databricks notebook source
import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.billboard.com/music/travis-scott/chart-history")

soup = BeautifulSoup(r.content,'lxml')

div = soup.find_all('div', {'class':'artist-section--chart-history__title-list'})[0]

df = pd.read_html(str(div))

print(df[0].to_json(orient='records'))

