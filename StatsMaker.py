from sportsreference.nfl.boxscore import Boxscores
import pandas as pd

game_data = Boxscores(1, 2020, 3)
df = game_data.games
df = pd.DataFrame.from_dict(df)
