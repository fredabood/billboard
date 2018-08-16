from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
import boto3
import json


def find_next_date(date):
    
    date = pd.to_datetime(date, format='%Y%m%d')

    if date >= datetime(1958,8,4):
        date = date + timedelta(1)

    else:
        date = datetime(1958,8,4)

    return date


def save_html(chart, bucket, date=None):
    
    '''
    Read webpage to BeautifulSoup from internet.
    '''
    # Generate URL to scrape
    url = f"https://www.billboard.com/charts/{chart}"
    
    if date:
        url = url + f"/{date.strftime('%Y-%m-%d')}"
    
    # Read webpage, Convert to text, Convert to soup
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    
    '''
    Sending BeautifulSoup to S3 as a HTML file.
    '''
    # Save webpage to local .html file named for date
    if date:
        bucket_key=f"{chart}/{date.strftime('%Y%m%d')}.html"
    else:
        bucket_key=f"{chart}/{datetime.now().strftime('%Y%m%d')}.html"
    
    filename = 'data.html'
    
    f = open(filename,'w')
    f.write(str(soup))
    
    # Upload .txt file to S3
    bucket.upload_file(filename, Key=bucket_key)
    
    # Delete local .txt file
    os.remove(filename)


if __name__ == "__main__":
    
    '''
    Webpage > HTML
    '''

    s3 = boto3.resource('s3')
    resource = boto3.resource('s3') # high-level object-oriented API
    
    bucket = 'billboard-charts-html'
    bucket = resource.Bucket(bucket)
    
    with open('charts.json') as log:
        charts = json.load(log)
    
    # Save webpages to HTML files on S3 bucket
    for category in charts:
        for chart in charts[category]:
    
            date = charts[category][chart]
            
            if date > 0:

                date = find_next_date(date)

                while date <= datetime.now():
                    save_html(chart=chart, bucket=bucket, date=date)
                    charts[category][chart] = int(date.strftime('%Y%m%d'))
                    date += timedelta(1)
                    
                    with open('charts.json', 'w') as log:
                        json.dump(charts, log)
            else:

                save_html(chart=chart, bucket=bucket)
                    
                with open('charts.json', 'w') as log:
                    json.dump(charts, log)