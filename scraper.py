from datetime import datetime, timedelta
import boto3
import json

from scrape_funcs import find_next_date, save_html


if __name__ == "__main__":

    '''
    Webpage > HTML
    '''

    s3 = boto3.resource('s3')
    resource = boto3.resource('s3')  # high-level object-oriented API

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
                    print(chart + ': ' + date.strftime('%Y-%m-%d') + '\n')

                    date += timedelta(1)

                    with open('charts.json', 'w') as log:
                        json.dump(charts, log)

            else:

                save_html(chart=chart, bucket=bucket)

                with open('charts.json', 'w') as log:
                    json.dump(charts, log)
