

import json
import urllib2
import mlb_database

BASE_MLB_GAME_URL = "http://gd2.mlb.com/components/game/mlb/"


class MLBData(object):
    """
    Base representation of mlb data
    """
    def __init__(self, date):
        self.game_year = date['year']
        self.game_month = date['month']
        self.game_date = date['day']

    def get_url(self):
        year = "year_" + self.game_year
        month = "/month_" + self.game_month
        day = "/day_" + self.game_date
        return BASE_MLB_GAME_URL + year + month + day

    def get_dates(self):
        """
        Get list of days in month
        """
        pass

    def get_teams(self, data):
        """
        Get Teams that played on date specified
        """
        teams = {}
        # print data['away_team_name'], data['away_team_id']
        teams[data['home_team_name']] = data['home_team_id']
        teams[data['away_team_name']] = data['away_team_id']
        mlb_database.MLB_DB().add_teams(teams)

    def get_team_runs(self, data):
        """
        Get Team Stat
        """
        team_score = {}
        for k, v in data.items():
            if 'linescore' in k:
                team_score[data['home_team_id']] = v['r']['home']
                team_score[data['away_team_id']] = v['r']['away']
        mlb_database.MLB_DB().add_score(team_score)

    def parse_scoreboard(self, data):
        """
        parse data for gameday
        """

        for k, v in data.iteritems():
            if "home_team_name" in k:
                home_team = v
            if "home_team_id" in k:
                home_team_id = v
            if "linescore" in k:
                home_team_score = v['r']['home']
                away_team_score = v['r']['away']
            if "away_team_name" in k:
                away_team = v
            if "away_team_id" in k:
                away_team_id = v
        # print "Home Team:  {} [{}] Score: {} VS Away Team: {} [{}] Score: {}".format(
        #     home_team,
        #     home_team_id,
        #     home_team_score,
        #     away_team,
        #     away_team_id,
        #     away_team_score
        #     )

    def get_scoreboard(self, url):
        """
        Get master_scoreboard data
        """
        game_file = (url + "/master_scoreboard.json")
        game_file = urllib2.urlopen(game_file)
        # game_file = game_file.read()
        data_file = json.loads(game_file.read())
        for k, v in data_file['data']['games'].iteritems():
            if 'game' in k:
                for game_data in v:
                    self.get_teams(game_data)
                    self.get_team_runs(game_data)
                    # self.parse_scoreboard(game_data)



