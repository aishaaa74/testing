
 
import pytest
from guess_number import (
    parse_guess,
    is_in_range,
    check_guess,
    GuessNumberGame,
    MIN_NUMBER,
    MAX_NUMBER,
)
 
 

def test_parse_guess_valid_number():
    assert parse_guess("42") == 42
 
 
def test_parse_guess_strips_spaces():
    assert parse_guess("  17 ") == 17
 
 
def test_is_in_range_inside_bounds():
    assert is_in_range(50) is True
 
 
def test_is_in_range_lower_boundary():
    assert is_in_range(MIN_NUMBER) is True
 
 
def test_is_in_range_upper_boundary():
    assert is_in_range(MAX_NUMBER) is True
 
 
def test_check_guess_equal():
    assert check_guess(50, 50) == "equal"
 
 
def test_check_guess_greater():
    assert check_guess(30, 70) == "greater"
 
 
def test_check_guess_less():
    assert check_guess(70, 30) == "less"
 
 
def test_game_correct_guess_wins():
    game = GuessNumberGame(secret=42)
    outcome = game.make_guess("42")
 
    assert outcome["status"] == "ok"
    assert outcome["result"] == "equal"
    assert outcome["won"] is True
    assert game.is_finished is True
 
 
def test_game_wrong_guess_gives_hint_and_continues():
    game = GuessNumberGame(secret=42)
    outcome = game.make_guess("10")
 
    assert outcome["status"] == "ok"
    assert outcome["result"] == "greater"
    assert game.is_finished is False
    assert outcome["attempts_left"] == game.max_attempts - 1
 
 
def test_game_runs_out_of_attempts():
    game = GuessNumberGame(secret=42, max_attempts=3)
    game.make_guess("1")
    game.make_guess("2")
    outcome = game.make_guess("3")
 
    assert game.is_finished is True
    assert game.is_won is False
    assert outcome["attempts_left"] == 0
 
 

def test_parse_guess_letters_raises_error():
    with pytest.raises(ValueError):
        parse_guess("abc")
 
 
def test_parse_guess_empty_string_raises_error():
    with pytest.raises(ValueError):
        parse_guess("")
 
 
def test_parse_guess_float_raises_error():
    with pytest.raises(ValueError):
        parse_guess("3.5")
 
 
def test_is_in_range_number_too_small():
    assert is_in_range(0) is False
 
 
def test_is_in_range_number_too_large():
    assert is_in_range(101) is False
 
 
def test_is_in_range_negative_number():
    assert is_in_range(-5) is False
 
 
def test_game_non_numeric_input_does_not_spend_attempt():
    game = GuessNumberGame(secret=42)
    outcome = game.make_guess("не число")
 
    assert outcome["status"] == "error"
    # Некорректный ввод не должен тратить попытку игрока
    assert game.attempts_used == 0
 
 
def test_game_out_of_range_input_returns_error():
    game = GuessNumberGame(secret=42)
    outcome = game.make_guess("500")
 
    assert outcome["status"] == "error"
    assert game.attempts_used == 0
 
 
def test_game_move_after_finish_returns_error():
    game = GuessNumberGame(secret=42)
    game.make_guess("42")  
    outcome = game.make_guess("10")
    assert outcome["status"] == "error"
 
