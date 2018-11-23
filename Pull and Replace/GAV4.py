# Shamelessly stolen mostly from Hello Analytics Reporting API V4.

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
import sqlite3

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
          'dateRanges': [{'startDate': '90daysAgo', 'endDate': 'today'}],
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
    global listings
    listings = reports['columnHeader']['dimensions']
    for metrics in reports['columnHeader']['metricHeader']['metricHeaderEntries']:
      listings.append(metrics['name'])
    global datas
    datas = []
    for data_raw in reports['data']['rows']:
      for dimensions in data_raw['dimensions']:
        datas.append(dimensions)
      for metrics in data_raw['metrics']:
        for values in metrics['values']:
          datas.append(values)
  # uses np to reshape the listings into a dataframe whose size is determined by what's pulled
  df= pd.DataFrame(np.array(datas).reshape(int(len(datas)/len(listings)),len(listings)), columns=listings)
  # fixes date
  df['ga:date'] = pd.to_datetime(df['ga:date'].astype(str)).dt.strftime('%m/%d/%y')
  return(df)

def merge(data_in, data_out):
  #pulls current CSV
  df2 = pd.read_csv(data_out)
  
  #if this is the first run, it sets up the columns in the output file
  if list(df2.columns.values) != ['ga:date', 'ga:source', 'ga:medium', 'ga:sessions', 'ga:bounces']:
    df2 = columns = ['ga:date', 'ga:source', 'ga:medium', 'ga:sessions', 'ga:bounces']
  
  #sets up sqlite DB locally
  conn = sqlite3.connect(':memory:')
  
  #not currently used, but there just in case
  cursor = conn.cursor()
  
  #importing the datasets
  df2.to_sql('t', conn, if_exists = 'append', index = False)
  data_in.to_sql('t', conn, if_exists = 'append', index = False)
  
  #filters the latest data with the option to rename the columns to whatever is preffered
  df3 = pd.read_sql_query('SELECT [ga:date], [ga:source], [ga:medium], max([ga:sessions]) AS [ga:sessions], [ga:bounces] FROM t Group BY [ga:date], [ga:source]', conn)
  
  #sorts
  df3 = df3.sort_values(['ga:date', 'ga:source', 'ga:medium'])
  
  #closes the local sqlite server
  conn.close()

  df3.to_csv(data_out, index = False)

def main():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  new_data = write_response(response)
  merge(new_data, 'Out.csv')
  


if __name__ == '__main__':
  main()
