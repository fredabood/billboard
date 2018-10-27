import json
import glob
import boto3

'''
Shifting to centralized S3 log storage
'''

client = boto3.client('s3')  # low-level functional API
resource = boto3.resource('s3')  # high-level object-oriented API
bucket = resource.Bucket('billboard-logs')  # subsitute for your s3 bucket name
files = list(bucket.objects.filter())

charts = {}

keys = []
for file in files:
    keys.append(file.key.replace('.json', ''))

for key in keys:
    partial_chart = list(bucket.objects.filter(Prefix=key))[0]
    charts[key] =

json.loads(file.get()['Body'].read().decode('utf-8'))

'''
Local log storage
'''

paths = glob.glob('./charts/*.json')


def assemble_chart(broken_log_dir=paths, agg_log_file='charts.json'):

    charts = {
      "Greatest of All Time": json.loads(broken_log_dir + '/greatest.json')[0],
      "Top Charts": json.loads(broken_log_dir + '/topcharts.json')[0],
      "Breakign & Entering": json.loads(broken_log_dir + '/emerging.json')[0],
      "Christian/Gospel": json.loads(broken_log_dir + '/christian.json')[0],
      "Country": json.loads(broken_log_dir + '/country.json')[0],
      "Dance/Electronic": json.loads(broken_log_dir + '/dance.json')[0],
      "Holiday": json.loads(broken_log_dir + '/holiday.json')[0],
      "International": json.loads(broken_log_dir + '/international.json')[0],
      "Latin": json.loads(broken_log_dir + '/latin.json')[0],
      "Pop": json.loads(broken_log_dir + '/pop.json')[0],
      "R&B/Hip-Hop": json.loads(broken_log_dir + '/hiphop.json')[0],
      "Rock": json.loads(broken_log_dir + '/rock.json')[0],
      "Web": json.loads(broken_log_dir + '/web.json')[0],
      "Additional Genres": json.loads(broken_log_dir + '/additional.json')[0]
    }

    with open(agg_log_file, 'w') as log:
        json.dump(charts, log)

    return charts
