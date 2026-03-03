
data = {
        'players': {
            'alice': {'level': 41, 'total_score': 2824, 'sessions_played': 13,
                      'favorite_mode': 'ranked', 'achievements_count': 5},
            'bob': {'level': 16, 'total_score': 4657, 'sessions_played': 27,
                    'favorite_mod': 'ranked', 'achievements_count': 2},
            'ellie': {'level': 44, 'total_score': 9935, 'sessions_played': 21,
                      'favorite_mod': 'ranked', 'achievements_count': 7},
            'diana': {'level': 3, 'total_score': 1488, 'sessions_played': 21,
                      'favorite_mod': 'casual', 'achievements_count': 4},
            'eve': {'level': 33, 'total_score': 1434, 'sessions_played': 81,
                    'favorite_mod': 'casual', 'achievements_count': 7},
            'frank': {'level': 15, 'total_score': 8359, 'sessions_played': 85,
                      'favorite_mod': 'competitive', 'achievements_count': 1}
            },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
                'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
                'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
                'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
                'mode': 'ranked', 'completed': True},
            {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
                'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
                'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
                'mode': 'casual', 'completed': True},
            {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
                'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
                'mode': 'casual', 'completed': False},
            {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
                'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
                'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
                'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 46, 'score': 329,
                'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
                'mode': 'casual', 'completed': True},
            {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
                'mode': 'casual', 'completed': False},
            {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
                'mode': 'competitive', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
                'mode': 'ranked', 'completed': False},
            {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
                'mode': 'ranked', 'completed': False},
            {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
                'mode': 'ranked', 'completed': False},
            {'player': 'alice', 'duration_minutes': 101, 'score': 292,
                'mode': 'casual', 'completed': True},
            {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
                'mode': 'competitive', 'completed': True},
            {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
                'mode': 'competitive', 'completed': False},
            {'player': 'eve', 'duration_minutes': 115, 'score': 147,
                'mode': 'ranked', 'completed': True},
            {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
                'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
                'mode': 'casual', 'completed': False},
            {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
                'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
                'mode': 'competitive', 'completed': True},
            {'player': 'bob', 'duration_minutes': 52, 'score': 761,
                'mode': 'ranked', 'completed': True},
            {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
                'mode': 'casual', 'completed': True},
            {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
                'mode': 'casual', 'completed': True}
            ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked'
            ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer'
            ]
        }

def list_comprehension():
    highscores = set()
    for num in data['sessions']:
        if num['score'] > 2000:
            highscores.add(num['player'])
    print(list(highscores))
    

def double_highscore():
    highscore = set()
    for num in data['sessions']:
        if num['score'] > 2500:
            num['score'] = num['score'] * 2
            highscore.add(num['score'])
    print(list(highscore))

def player():
    players = set()
    for names in data['sessions']:
        players.add(names['player'])
    print(list(players))

def dict_scores():
    output = []
    for name, info in data["players"].items():
        output.append(f"{name}: {info['total_score']}")

    print(", ".join(output))

def score_categories():
    scores =  {
        'low': 0,
        'medium': 0,
        'high': 0
    }
    for name, info in data["players"].items():
        if info['total_score'] > 5000:
            scores['high'] += 1
        elif info['total_score'] > 2000:
            scores['medium'] += 1
        elif info['total_score'] > 1000:
            scores['low'] += 1
    print(scores)

def achievement_counts():
    result = dict()

    for name, info in data["players"].items():
        result[name] = info["achievements_count"]
    print(f"Achievement counts: {result}")

def set_comprehension():
    uniqueplayer = set()
    uniqueachievements = set()
    mode = dict()

    for names in data['sessions']:
        uniqueplayer.add(names['player'])

    for names in data['achievements']:
        uniqueachievements.add(names)

    for name, info in data["players"].items():
        fav = info.get("favorite_mod")
        if fav is None:
            fav = info.get("favorite_mode")
        mode[name] = fav

    print(uniqueplayer)
    print(uniqueachievements)
    print(mode)

def combined_analysis():
    

def main():
    print("=== Game Analytics Dashboard ===\n")
    print("=== Game Analytics Dashboard ===")
    list_comprehension()
    double_highscore()
    player()
    print("\n=== Dict Comprehension Examples ===")
    dict_scores()
    score_categories()
    achievement_counts()
    print("=== Set Comprehension Examples ===")
    set_comprehension()
    
if __name__ == "__main__":
    main()