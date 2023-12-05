def part1(games):
    part1=0
    MAX = {'red': 12, 'green':13, 'blue':14}
    for game in games:
        bad_game = False
        key = game.split(":")[0].split(" ")[1].strip()

        # Create Game Dictionary
        for sets in game.split(": ")[1].split("; "):
            num_ball = {}
            selections = sets.split(', ')
            for pair in selections:
                num_ball[pair.split(" ")[1]] = int(pair.split(" ")[0])

            # Evaluate on each color's largest number
            for color in num_ball:
                if num_ball[color] > MAX[color]:
                    bad_game=True
                    break
        
        if not bad_game:
            part1+=int(key)
    return part1

def part2(games):
    part2=0
    for game in games:
        
        # Create Game Dictionary
        max_color = {"blue": 0, "red":0, "green":0}
        game = game.strip()
        for sets in game.split(": ")[1].split("; "):
            num_ball = {}
            selections = sets.split(', ')
            for pair in selections:
                num_ball[pair.split(" ")[1]] = int(pair.split(" ")[0])

        # Evaluate on color
            for color in num_ball:
                if num_ball[color] > max_color[color]:
                    max_color[color] = num_ball[color]

        power=1
        for val in max_color.values():
            power*=val
        part2+=power
    return part2
