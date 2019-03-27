"""test."""
import highscor


def test_highscor():
    game = "snake"
    highscor.create_game_file(game, 5, True)
    highscor.write_score(game, "me", 24)
    scores = highscor.list_scores(game)
    print(scores)


test_highscor()
