"""test."""
import highscor


def test_highscor():
    game = "snake"
    print("0")
    result = highscor.create_game_file(game, 5, True)
    print(result)
    print("1")
    highscor.write_score(game, "me", 24)
    print("2")
    scores = highscor.list_scores(game)
    print(scores)


test_highscor()
