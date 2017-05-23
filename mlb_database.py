
import sqlite3
import os


class MLB_DB(object):
    """
    Database Setup
    """
    _db_conn = None
    _db_cur = None

    def __init__(self, dbname='databases/default.db'):
        self.dbname = dbname
        self.dbtable = "team_data"
        self._db_conn = sqlite3.connect(self.dbname)
        self._db_cur = self._db_conn.cursor()
        self.create_db_table()

    def create_db_table(self):
        """
        Create database and table
        """
        # Create table
        self._db_cur.execute('''CREATE TABLE IF NOT EXISTS %s
             (team_id INT UNIQUE, team_name VARCHAR, score_0 INT DEFAULT '0',
             score_1 INT DEFAULT '0', score_2 INT DEFAULT '0', 
             score_3 INT DEFAULT '0', score_4 INT DEFAULT '0',
             score_5 INT DEFAULT '0', score_6 INT DEFAULT '0',
             score_7 INT DEFAULT '0', score_8 INT DEFAULT '0',
             score_9 INT DEFAULT '0', score_10 INT DEFAULT '0',
             score_11 INT DEFAULT '0', score_12 INT DEFAULT '0',
             score_13 INT DEFAULT '0')''' % self.dbtable)

    def add_team_query(self, data):
        """
        asdf
        """
        pass

    def add_teams(self, data):
        """
        Add Teams to DB
        """
        for k, v in data.items():
            try:
                self._db_cur.execute("insert or ignore into team_data \
                (team_id, team_name) values (?, ?)", (v, k))
                self._db_conn.commit()
            except sqlite3.Error as er:
                print er

    def add_score(self, data):
        """
        Add Team Score via Team ID
        """
        # sql_score_add = """update $s SET
        for team_id, score in data.items():
            if int(score) in range(0, 14):
                column = "score_" + (score)
                sql_cmd = ("UPDATE %s SET %s=1 WHERE team_id=%s" % (self.dbtable, column, team_id))
                print sql_cmd
                try:
                    self._db_cur.execute(sql_cmd)
                    self._db_conn.commit()
                except sqlite3.Error as er:
                    print er





