import os

from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

APP_PATH = os.path.join(os.path.dirname(__file__), "..", "app.py")

def test_range_caption_updates_when_difficulty_changes():
    at = AppTest.from_file(APP_PATH)
    at.run()

    # Default difficulty is "Normal"
    assert at.sidebar.caption[0].value == "Range: 1 to 100"

    at.sidebar.selectbox[0].select("Easy").run()
    assert at.sidebar.caption[0].value == "Range: 1 to 20"

    at.sidebar.selectbox[0].select("Hard").run()
    assert at.sidebar.caption[0].value == "Range: 1 to 50"

    at.sidebar.selectbox[0].select("Normal").run()
    assert at.sidebar.caption[0].value == "Range: 1 to 100"

def test_secret_updates_within_new_range_when_difficulty_changes():
    at = AppTest.from_file(APP_PATH)
    at.run()

    # Default difficulty is "Normal" (range 1 to 100)
    assert 1 <= at.session_state["secret"] <= 100

    at.sidebar.selectbox[0].select("Easy").run()
    # Easy range is 1 to 20, so the secret should be updated to fall within it
    secret = at.session_state["secret"]
    assert 1 <= secret <= 20

    # Developer Debug Info dropdown should reflect the same updated secret
    debug_values = [item.value for item in at.expander[0].markdown]
    assert f"Secret: `{secret}`" in debug_values

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"
    assert result[1] == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High", "Go Lower"
    result = check_guess(60, 50)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low", "Go Higher"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"