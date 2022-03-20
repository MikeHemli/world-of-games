from live import load_game, welcome
from Scores.score import add_score
from check_victory import check_victory
print(welcome())
results = load_game()


check_victory(results[1])
add_score(results[1])
