from google.cloud import bigquery
from resources.queries import SQLQuery
from resources.common import Common
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
        response=[]
        for row in query_job:
            response.append({
                'full_visitor_id': row['fullvisitorid'], 
                'address_changed': row['address_changed'],
                'is_order_placed': row['is_order_placed'], 
                'is_order_delivered': row['is_order_delivered'], 
                'application_type': row['operatingSystem']
            })
        return response
    
    def process_job_by_visitor_id(self, fullvisitorId):
        try:
            logging.info("Querying data from the Dataset to analyze")
            query = SQLQuery().get_stmt_for_order_location_analytics(fullvisitorId)
            query_job = self.get_query_job_result(query)
            return Common().response(self.get_location_order_analytics(query_job))
        except Exception as e:
            logging.error(e)
            return Common.response_error(e)