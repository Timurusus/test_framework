from datetime import datetime
import logging


class Result:
    def __init__(self):
        self.log_file_path = 'results/result.log'
        logging.basicConfig(filename=self.log_file_path,
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger("TestFramework")
        self.logger.setLevel(logging.DEBUG)

    def start_test(self, file_name):
        global start_dt
        start_dt = datetime.now()
        self.logger.info(f'Testing of {file_name} was started')

    def finish_test(self):
        finish_dt = datetime.now()
        self.logger.info(f'Testing is finished')
        date_dif = finish_dt - start_dt
        self.logger.info(f'TestFrameworks runtime is {date_dif}')

    def start_case(self, test_name):
        self.logger.info(f'Test case "{test_name}"')

    def add_pass(self, query, actual_result):
        self.logger.info(f'PASS. Result is {actual_result} as expected'
                         f'\n\tQuery: {query}')




