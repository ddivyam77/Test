from project import get_user_choice, get_computer_choice, determine_winner

def test_get_user_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "rock")
    assert get_user_choice() == "rock"

def test_get_computer_choice():
    assert get_computer_choice() in ["rock", "paper", "scissors"]

def test_determine_winner():
    assert determine_winner("rock", "scissors") == "win"
    assert determine_winner("rock", "paper") == "loss"
    assert determine_winner("rock", "rock") == "tie"
