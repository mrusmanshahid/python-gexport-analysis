import logging
from resources.google_analytics import GoogleAnalytics
import unittest
import argparse
from argparse import ArgumentParser

if __name__ == "__main__":

   parser = ArgumentParser(description='argument parser for analytics')
   parser.add_argument('--full_visitor_id', default=False, required=True, help='fullvisitorId to process data')
   parser.add_argument('--run_test', default=False, action='store_true', help='Hyper parameter to validate test result')
   parser.set_defaults(run_test=False)
   parsed_args = parser.parse_args()

   if parsed_args.run_test:
      logging.info("Performing Unit Test Cases")
      suite = unittest.TestLoader().discover('.', pattern = "*_test.py")
      unittest.TextTestRunner(verbosity=2).run(suite)

   if parsed_args.full_visitor_id:
      response = GoogleAnalytics().process_job_by_visitor_id(parsed_args.full_visitor_id)
      print(response)
