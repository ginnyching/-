def win_percenatge(info):
    home = 0
    away = 0
    total = 0
    for i in info:
        #count the total games played
        total += 1
        #home+1 when home team wins, else away+1
        if float(i['home_final_score']) > float(i['away_final_score']):
            home += 1
        else:
            away += 1
    #print(total,home,away)

    print('主場勝率:', home / total)
    print('客場勝率:', away / total)

    if home>away:
        print('主場勝率較高')
    else:
        print('客場勝率較高')

#type of info={team/venue name:[win,lose]}
def highest_win_rate(info):
    rate = 0
    team = ''
    # find the team/venue with highest win rate(win/win+lose)
    for i in info:
        cur = int(info[i][0]) / (int(info[i][0]) + int(info[i][1]))
        if cur > rate:
            rate = cur
            team = i
    return team
