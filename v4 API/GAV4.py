# Shamelessly stolen mostly from Hello Analytics Reporting API V4.

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '<GOOGLE ANALYTICS SECRET HERE>'
VIEW_ID = '<VIEW ID HERE>'


def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:bounces'}], 
          'dimensions': [{'name': 'ga:date'}, {'name': 'ga:source'}, {'name': 'ga:medium'}]
        }]
      }
  ).execute()


def write_response(response):
  """Parses and prints the Analytics Reporting API V4 response.

  Most of this is just unpacking the nightmare that is the response
  I'm sure something somewhere makes better use of it than I did here
  """
  
  for reports in response['reports']:
    global list
    list = reports['columnHeader']['dimensions']
    for metrics in reports['columnHeader']['metricHeader']['metricHeaderEntries']:
      list.append(metrics['name'])
    global datas
    datas = []
    for data_raw in reports['data']['rows']:
      for dimensions in data_raw['dimensions']:
        datas.append(dimensions)
      for metrics in data_raw['metrics']:
        for values in metrics['values']:
          datas.append(values)
  # uses np to reshape the list into a dataframe whose size is determined by what's pulled
  df= pd.DataFrame(np.array(datas).reshape(int(len(datas)/len(list)),len(list)), columns=list)
  # fixes date
  df['ga:date'] = pd.to_datetime(df['ga:date'].astype(str)).dt.strftime('%m/%d/%y')
  df.to_csv('GA-V4.csv', index = False)

def main():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  write_response(response)


if __name__ == '__main__':
  main()
