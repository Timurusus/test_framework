
class Configurator:
    def __init__(self, env):
        with open('config.json') as f:
            self.config = eval(f.read())
        self.config = self.config[env]

    def get_driver_name(self):
        return self.config['driver']

    def get_server_name(self):
        return self.config['server_name']

    def get_database_name(self):
        return self.config['database']

    def get_test_data_folder(self):
        return self.config['test_data_folder']


