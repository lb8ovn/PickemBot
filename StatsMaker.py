from sportsreference.nfl.boxscore import Boxscores
import pandas as pd

CURRENT_YEAR = 2020

def getGameResults(team1, team2, week):
    weekly_games = (Boxscores(week, CURRENT_YEAR)).games
    for game_week in weekly_games:
        for game in game_week[game_week]:
            if game['away_abbr'] == team1 and game['home_abbr'] == team2:
                return game


def getSeasonStatsForGame(team1, team2, week):
    return False

if __name__ == "__main__":

    buf_at_lv_results = getGameResults('buf', 'rai', 4)
    if buf_at_lv_results['winning_abbr'] == 'buf' and buf_at_lv_results['home_score'] == 23:
        print('good work')
    else:
        print("jeezoos... read a f'n book")

    den_at_atl_results = getGameResults('den', 'atl', 9)
    if den_at_atl_results['losing_abbr'] == 'den' and den_at_atl_results['away_score'] == 27:
        print('good work')
    else:
        print("jeezoos... read a f'n book")

    ## We will get to these later...
    #buf_at_lv = getSeasonStatsForGame('BUF', 'LV', 4)

    #chi_at_car = getSeasonStatsForGame('CHI', 'CAR', 5)
