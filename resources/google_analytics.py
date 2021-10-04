from google.cloud import bigquery
from resources.queries import SQLQuery
from resources.common import Common
import logging

class GoogleAnalytics:

    def __init__(self):
        self.client = bigquery.Client()
        self.common = Common()

    # the method is initializes the query within the client 
    # for execution and returns the query job to users to proceed.
    def get_query_job_result(self, query):
        try:    
            logging.info("Querying data from the Dataset to analyze")
            query_job = self.client.query(query)
            return query_job
        except Exception as e:
            logging.error("Query failed due to the error below")
            logging.error(e)

    # the method wraps the response result in to desired output format and 
    # appends the wrapped object in the response array. the method takes query job as input 
    # and iterates over it to prepare response.
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

    # the method acts as a central layer which combines all the unit methods 
    # at one place for the consumer to response the method takes fullVisitorId 
    # as input and return response array as an output.
    def process_job_by_visitor_id(self, fullvisitorId):
        try:
            logging.info("Querying data from the Dataset to analyze")
            query = SQLQuery().get_stmt_for_order_location_analytics(fullvisitorId)
            query_job = self.get_query_job_result(query)
            data = self.get_location_order_analytics(query_job)
            if self.common.validate_empty(data):
                return self.common.response_empty(data)
            return self.common.response(data)
        except Exception as e:
            logging.error(e)
            return self.common.response_error(e)
