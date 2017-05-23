#!/usr/bin/env python


import argparse
from datetime import datetime
import sys
import mlb
import mlb_database
import os


def parse_args():
    """
    Parse command line options
    """
    parser = argparse.ArgumentParser(
        prog='mlbpool',
        description='mlb pool app to get current team stats (wins vs losses)'
    )
    parser.add_argument('-d', '--date', dest='cmd_date',
                        help='Specify date you want to see stats\
                        for "example: YYYYMMDD"'
                       )

    args = parser.parse_args()

    return args


def validate_date(date):
    """
    Ensure date is a acceptable valid date
    """
    try:
        date = datetime.strptime(date, "%Y%M%d")
    except ValueError:
        msg = "Incorrect data format, should be YYYYMMDD or YYYYMMD"
        sys.exit(msg)
    return date.strftime("%Y%M%d")


def get_mlb_date(valid_date):
    """
    Return YYYY, DD, MM data
    """
    year = valid_date[0:4]
    month = valid_date[4:6]
    day = valid_date[6:8]
    return {"year": year, "month": month, "day": day}


def main():
    """
    RUN MLB APP
    """
    args = parse_args()

    # Create DB
    mlb_database.MLB_DB()
    game_date = get_mlb_date(validate_date(args.cmd_date))
    mlb_data = mlb.MLBData(game_date)
    mlb_data.get_scoreboard(mlb_data.get_url())
    print mlb_database.MLB_DB()._db_conn.close()



if __name__ == '__main__':
    main()
