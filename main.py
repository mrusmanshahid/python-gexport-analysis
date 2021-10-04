
from resources.google_analytics import GoogleAnalytics
from unit_tests.google_analytics import TestGoogleAnalytics
import unittest
from argparse import ArgumentParser

if __name__ == "__main__":
   unittest.main()
   parser = ArgumentParser(description='Argument parser for PG restore')
   parser.add_argument('--full_visitor_id', default=None, required=True, help='fullvisitorId to process data')
   parser.add_argument('--run_test', default=None, required=False, help='Hyper parameter to validate test result')
   parsed_args = parser.parse_args()
   #x=GoogleAnalytics().process_job_by_visitor_id("634908280670541439")
   # print(x)
