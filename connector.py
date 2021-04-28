import pyodbc


class Connector:
    def __init__(self, driver, server, database):
        conn = pyodbc.connect(driver=driver,
                              server=server,
                              database=database
                              )
        self.cursor = conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
