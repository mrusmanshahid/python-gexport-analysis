import os
import logging

class Config:

    def __init__(self):
        pass

    def load_configurations(self):
        self.set_logging_config()
        self.check_environment_variable_set()
        
    @staticmethod
    def set_logging_config():
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    @staticmethod
    def check_environment_variable_set():
        print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
        Config.is_environment_variable_set = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') != None
    