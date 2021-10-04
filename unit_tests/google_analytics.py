import unittest
import unittest.mock as mock
import logging
from resources.google_analytics import GoogleAnalytics

class TestGoogleAnalytics(unittest.TestCase):

    def test_process_job_by_visitor_id_no_visitor_id(self):
        ga = GoogleAnalytics()
        self.assertDictEqual(ga.process_job_by_visitor_id(""),{"status": 204, "response_message":"No data found", "response_code":"NO_CONTENT", "data": []})
        
    def test_process_job_by_visitor_id(self):
        ga = GoogleAnalytics()
        self.assertEqual(ga.process_job_by_visitor_id("634908280670541439"),{"status": 200, "response_message":"Success", "response_code":"SUCCESS", "data": mock.ANY })

if __name__ == '__main__':
    unittest.main()