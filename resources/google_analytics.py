from google.cloud import bigquery
from queries import SQLQuery
import logging

class GoogleAnalytics:

    def __init__(self):
        self.client = bigquery.Client()

    def get_query_job_result(self, query):
        try:    
            logging.info("Querying data from the Dataset to analyze")
            query_job = self.client.query(query)
            return query_job
        except Exception as e:
            logging.error("Query failed due to the error below")
            logging.error(e)

    def get_location_order_analytics(self, query_job):
        for row in query_job:
            # Row values can be accessed by field name or index.
            print("name={}, count={}".format(row[0], row["common_name"]))
    
    def process_job_by_visitor_id(self, fullvisitorId):
        try:
            fullvisitorId = int(fullvisitorId)
            logging.info("Querying data from the Dataset to analyze")
            query = SQLQuery().get_stmt_for_order_location_analytics("fullvisitorId")
            query_job = self.get_query_job_result(query)
            return self.get_location_order_analytics(query_job)
        except ValueError:
            logging.error('fullVisitorId should be integer')
            return None
        except Exception as e:
            logging.error(e)
            return None
