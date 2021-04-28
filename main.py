from sys import argv
from configurator import Configurator
from connector import Connector
from resulting import Result
from test_processor import TestProcessor


def run():
    config = Configurator(argv[1])
    driver_name = config.get_driver_name()
    server_name = config.get_server_name()
    database_name = config.get_database_name()

    connector = Connector(driver_name, server_name, database_name, "TsimurCharniauski", "1234")

    logger = Result()

    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()
    logger.finish_test()


if __name__ == '__main__':
    run()

