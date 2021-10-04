from resources.google_analytics import GoogleAnalytics
from unit_tests.google_analytics import TestGoogleAnalytics
import unittest
from argparse import ArgumentParser

if __name__ == "__main__":

   parser = ArgumentParser(description='Argument parser for PG restore')
   parser.add_argument('--full_visitor_id', default=None, required=True, help='fullvisitorId to process data')
   parser.add_argument('--run_test', default=None, type=bool, required=False, help='Hyper parameter to validate test result')
   parsed_args = parser.parse_args()

   if parsed_args.run_test:
      unittest.main()

   else:
      response = GoogleAnalytics().process_job_by_visitor_id(parsed_args.run_test)
      print(response)