import MySQLdb

class InvestDao:
    def __init__(self, host, port, user, passwd, db):
        self.conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)

    def sql(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

