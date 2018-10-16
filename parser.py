from bs4 import BeautifulSoup
import boto3
import json
import os

from parse_funcs import chart_gen


if __name__ == "__main__":
    client = boto3.client('s3')  # low-level functional API
    resource = boto3.resource('s3')  # high-level object-oriented API
    html_bucket = resource.Bucket('billboard-charts-html')  # subsitute this for your s3 bucket name.
    json_bucket = resource.Bucket('billboard-charts-json')

    prefix = 'hot-100'

    files = list(html_bucket.objects.filter(Prefix=prefix))

    for file in files:

        json_name = file.key.split('/')[-1].replace('html', 'json')

        file = file.get()['Body'].read().decode("utf-8")
        soup = BeautifulSoup(file, "html.parser")

        try:
            chart = chart_gen(soup)

            with open(json_name, 'w') as json_file:
                json.dump(chart, json_file)

            json_bucket.upload_file(json_name, Key=prefix + '/' + json_name)
            os.remove(json_name)

        except:
            pass
