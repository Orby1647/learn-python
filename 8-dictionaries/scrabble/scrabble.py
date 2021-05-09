letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}

letter_to_points[" "] = 0


def score_word(word):
    """takes in a word and calculates the score of the word"""
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                   "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for key, values in player_to_words.items():
    for word in player_to_words[key]:
        try:
            player_to_points[key] += score_word(word)
        except KeyError:
            player_to_points[key] = score_word(word)

print(player_to_points)