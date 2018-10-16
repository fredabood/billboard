import json
import glob

paths = glob.glob('./charts/*.json')

log_paths =

def assemble_chart(log_paths=paths, agg_log_file='charts.json'):

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
