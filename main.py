import logging
from resources.google_analytics import GoogleAnalytics
from resources.config import Config
import unittest
import argparse
from argparse import ArgumentParser

if __name__ == "__main__":

   parser = ArgumentParser(description='argument parser for analytics')
   parser.add_argument('--full_visitor_id', default=None, required=False, help='fullvisitorId to process data')
   parser.add_argument('--run_test', default=False, action='store_true', help='Hyper parameter to validate test result')
   parser.set_defaults(run_test=False)
   parsed_args = parser.parse_args()

   # load initial configurations for the application to run smoothly
   Config().load_configurations()
   
   # validating the google application credentials
   if not Config.is_environment_variable_set:
      logging.error("Please set Google Application Credentials by following the steps mentioned in the readme file. The program is exiting.")
      quit()

   # if the --run_test argument is provided then this section will execute 
   # and runs all the test cases within the project.
   if parsed_args.run_test:
      logging.info("Performing Unit Test Cases")
      suite = unittest.TestLoader().discover('.', pattern = "*_test.py")
      unittest.TextTestRunner(verbosity=2).run(suite)

   # if the --full_visitor_id argument is provided then this section will execute 
   # and prints the response output.
   if parsed_args.full_visitor_id:
      logging.info("Performing Analysis")
      response = GoogleAnalytics().process_job_by_visitor_id(parsed_args.full_visitor_id)
      print(response)
