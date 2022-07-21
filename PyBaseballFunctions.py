from pybaseball import statcast_pitcher, statcast_batter, playerid_lookup
from numpy import where
from GetUserInputs import *
from datetime import datetime
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

def stat_pitcher(firstp, lastp):
    year = (datetime.strftime(datetime.now(), "%Y"))
    month = (datetime.strftime(datetime.now(), "%m"))
    day = (datetime.strftime(datetime.now(), "%d"))
    start_dt = str(int(int(year)-5)) + '-' + month + '-' + day
    end_dt = year + '-' + month + '-' + day
    player_idp = playerid_lookup(lastp, firstp)
    if len(player_idp) == 0:
        data_p = ""
    else:
        data_p = statcast_pitcher(start_dt, end_dt, player_idp.iloc[0,2])
    return data_p

def stat_batter(firstb, lastb):
    year = (datetime.strftime(datetime.now(), "%Y"))
    month = (datetime.strftime(datetime.now(), "%m"))
    day = (datetime.strftime(datetime.now(), "%d"))
    start_dt = str(int(int(year)-5)) + '-' + month + '-' + day
    end_dt = year + '-' + month + '-' + day
    player_idb = playerid_lookup(lastb, firstb)
    if len(player_idb) == 0:
        data_b = ""
    else:
        data_b = statcast_batter(start_dt, end_dt, player_idb.iloc[0,2])
    return data_b

test = stat_batter('Will', 'Smith')

def pitcher_i(firstp, lastp):
    """
    Calculate pitcher's statistics from Statcast.

    Parameters
    ----------
    firstb: 'str'
        First name of pitcher.
    lastb: 'str'
        Last name of pitcher.
    """
    print('Gathering statistics for: ', firstp, lastp)
    h_pitches = {'count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'B': [38, 38, 37, 36, 31, 27, 26, 25, 25, 26, 26, 26],
        'C': [30, 16, 12, 11, 8, 5, 5, 5, 6, 6, 5, 7],
        'F': [11, 18, 20, 21, 24, 28, 28, 29, 29, 28, 28, 29],
        'S': [8, 12, 13, 13, 13, 13, 13, 13, 12, 13, 12, 11],
        'X': [12, 16, 18, 19, 23, 27, 27, 28, 28, 28, 28, 27]
        }

    historic_pitches = pd.DataFrame(h_pitches, columns= ['count', 'B', 'C', 'F', 'S', 'X'])

    data_p = stat_pitcher(firstp, lastp)

    if len(data_p) == 0:
        pitcher_dict = historic_pitches.to_dict()
        return pitcher_dict

    else:
        sub_pitch = data_p[["game_date", "pitcher", "batter", "events", "description", "inning"]]
        sub_pitch = sub_pitch.sort_index(ascending=False)
        sub_pitch["id"] = sub_pitch["batter"].astype(str) + "-" + sub_pitch["inning"].astype(str) + "-" + sub_pitch["game_date"].astype(str)

        sub_pitch["count"] = sub_pitch.groupby('id').cumcount() + 1

        y = pd.crosstab(sub_pitch['count'], sub_pitch['description']).apply(lambda r: r/r.sum(), axis=1)

        def check(col, table):
            if col in table:
                table[col] = table[col]
            else:
                table[col] = 0

        def delete(table):
            table.drop(table.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1, inplace=True)
            return table

        check('ball', y)
        check('blocked_ball', y)
        check('pitchout', y)
        check('called_strike', y)
        check('foul', y)
        check('foul_bunt', y)
        check('foul_tip', y)
        check('bunt_foul_tip', y)
        check('foul_pitchout', y)
        check('missed_bunt', y)
        check('swinging_strike', y)
        check('swinging_strike_blocked', y)
        check('swinging_pitchout', y)
        check('hit_into_play', y)
        check('hit_by_pitch', y)

        y['B'] = ( y['ball'] + y['blocked_ball'] + y['pitchout'] ) * 100
        y['C'] = ( y['called_strike'] ) * 100
        y['F'] = ( y['foul'] + y['foul_bunt'] + y['foul_tip'] + y['bunt_foul_tip'] + y['foul_pitchout'] ) * 100
        y['S'] = ( y['missed_bunt'] + y['swinging_strike'] + y['swinging_strike_blocked'] + y['swinging_pitchout'] ) * 100
        y['X'] = ( y['hit_into_play'] ) * 100

        y['B'] = y['B'].round(decimals=0)
        y['C'] = y['C'].round(decimals=0)
        y['F'] = y['F'].round(decimals=0)
        y['S'] = y['S'].round(decimals=0)
        y['X'] = y['X'].round(decimals=0)

        delete(y)
        y = y.reset_index()

        if y.shape[0] > 12:
            while y.shape[0] > 12:
                y = y.iloc[:-1]
        elif y.shape[0] < 12:
            while y.shape[0] < 12:
                new_line = historic_pitches[historic_pitches['count'] == y.shape[0] + 1]
                y = pd.concat([y, new_line], sort=False, ignore_index=True)
        else:
            y = y

        pitcher_dict = y.to_dict()
        return pitcher_dict

def batter_i(firstb, lastb):
    """
    Calculate batter's statistics from Statcast.

    Parameters
    ----------
    firstb: 'str'
        First name of batter.
    lastb: 'str'
        Last name of batter.
    """
    print('Gathering statistics for: ', firstb, lastb)
    h_atbats = {'FO': [58],
        'GO': [10],
        'S': [22],
        'D': [6],
        'T': [1],
        'HR': [3]
        }

    data_b = stat_batter(firstb, lastb)

    if len(data_b) == 0:
        batter_dict = h_atbats
        return batter_dict

    else:
        sub_bat = data_b[["game_date", "batter", "events", "description"]]
        sub_bat = sub_bat.loc[(sub_bat['events'].notna()) & (sub_bat['description'] == 'hit_into_play')]

        z = pd.crosstab(sub_bat['batter'], sub_bat['events']).apply(lambda r: r/r.sum(), axis=1)

        def check(col, table):
            if col in table:
                table[col] = table[col]
            else:
                table[col] = 0

        def delete_B(table):
            table.drop(table.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]], axis=1, inplace=True)
            return table

        check('catcher_interf', z) #single
        check('double', z) 
        check('double_play',z) #ground out
        check('field_error', z) #single
        check('field_out', z) #fly out
        check('fielders_choice', z) #single
        check('fielders_choice_out', z) #ground out
        check('force_out', z) #ground out
        check('game_advisory', z) 
        check('grounded_into_double_play', z) #ground out
        check('home_run', z)
        check('sac_bunt', z) #ground out
        check('sac_bunt_double_play', z) #ground out
        check('sac_fly', z) #fly out
        check('sac_fly_double_play', z) #fly out
        check('single', z)
        check('triple', z)
        check('triple_play', z) #ground out

        z['FO'] = ( z['field_out'] + z['sac_fly'] + z['sac_fly_double_play'] ) * 100
        z['GO'] = ( z['double_play'] + z['fielders_choice_out'] + z['force_out'] + z['grounded_into_double_play'] + z['sac_bunt'] + z['sac_bunt_double_play'] + z['triple_play'] ) * 100
        z['S']  = ( z['catcher_interf'] + z['field_error'] + z['fielders_choice'] + z['single'] ) * 100
        z['D']  = ( z['double'] ) * 100
        z['T']  = (z['triple'] ) * 100
        z['HR'] = (z['home_run'] ) * 100

        z['FO'] = z['FO'].round(decimals=0)
        z['GO'] = z['GO'].round(decimals=0)
        z['S']  = z['S'].round(decimals=0)
        z['D']  = z['D'].round(decimals=0)
        z['T']  = z['T'].round(decimals=0)
        z['HR'] = z['HR'].round(decimals=0)

        z = z.reset_index()
        delete_B(z)

        batter_dict = z.to_dict()
        return batter_dict