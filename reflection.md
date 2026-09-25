# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game was inconsistent. It gave me wrong messages for the guesses I gave.
  - Also the `New Game` button was not working as expected.
  - More on the bugs I found below.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Cannot press the key enter on my keyboard to submit | To submit my guess by pressing enter | Does not submit my guess and I have to click with my mouse | |
| When you change the difficulty in the sidenav, it does not update the low and high values in the blue box | The values to change since I updated the difficulty level | Does not change the values in the difficulty level| |
| Clicking the button `New Game` after winning or lossing does not restart a game | After winning a game, click on `New Game` button to start a new game | It does not start a new game. Forcing users to refresh the app | |
| Secret is 29, Guess number is 12 | The app tells me to guess lower | the app tells me to go higher | |
| Secret is 29, Guess number is 5 | The app tells me to guess lower | the app tells me to go higher | |
| Secret is 29, Guess number is 0 | The app should not handle `0` since it is invalid input | the app tells me to go lower | |
| Secret is 29, Guess number is 900 | The app should not handle `900` since it is invalid input | the app tells me to go higher | |

---

## 2. How did you use AI as a teammate?

**Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?**

- Use Claude Code

**Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).**

For the bug that I found *When you change the difficulty in the sidenav, it does not update the low and high values in the blue box*, I used the LLM to generate a unit test in the `test_game_logic.py` file called `test_range_caption_updates_when_difficulty_changes`. I did not know how to use the pytest framework to test the UI state changes. Now I have a better idea on how to test!

LLM suggested code:
```python
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
```

I verified the result by:
- first checking the code to see if it read correctly
- running the unit test
- verifying the UI changed when running app. 

**Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.**

When trying to fix the `check_guess` function and I was giving this suggestion:
```python
The TypeError happens because guess and secret don't always arrive as the same type — and it's not something check_guess controls, it's injected by the caller.

Where it comes from: parse_guess always returns guess as an int. But in app.py (lines 163–166), secret gets converted to a str on even attempts and left as int on odd ones:


if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)
else:
    secret = st.session_state.secret
So check_guess(guess_int, secret) gets int vs str half the time. Comparing int > str raises TypeError, which is why you see it bounce between the try and except blocks. guess is always an int — secret is the inconsistent one.

The real fix is in app.py: that type-toggling logic serves no purpose — it just randomly corrupts secret's type every other guess. Delete it and always keep secret as an int:


secret = st.session_state.secret
outcome, message = check_guess(guess_int, secret)
Belt-and-suspenders in logic_utils.py: normalize types at the top of check_guess so it's robust even if a str sneaks in, and drop the try/except entirely (it's using exceptions for control flow, which is what caused the bug to be surprising in the first place):


def check_guess(guess, secret):
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"
This removes the whole try/except path — no more silent lexicographic string comparisons, no more branch alternating on attempt parity.

Want me to apply both edits (app.py's secret-toggle removal and the logic_utils.py rewrite)?
```

The suggestion was good, it did pointed to the wrong line numbers. It must have gotten confused since the `app.py` file did not have `163` lines of code. I just read the code and found the place it refer to, but it gave me the wrong line numbers.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  - I decided whether a bug was fixed when my tests pass successfully and looking at the UI where I tested what I proposed in the unit test

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  - After importing the functions into `logic_utils.py` and fixing that, I ran the following tests `test_winning_guess`, `test_guess_too_high`, `test_guess_too_low`. After printing out and playing with the app, I realized that the tests had missing asserts. Asserting on result[0] was correct, but it was missing asserting on result[1]. There you can see that there is a bug. The messages were swapped.

- Did AI help you design or understand any tests? How?

  - LLMs did help in designing a test. They help me understand how to write a test to check for UI state change. You can see the LLM generate code in this unit test `test_range_caption_updates_when_difficulty_changes`

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

To my understanding, Streamlit is a python library that allows us to create UI using pure Python. The functionality of `rerun` is that it will rerun the script immediately. So when you call `st.rerun()`, it will not execute any other code after it and rerun the script

To me session state refers to the state of the UI, so for example, when the user inputted a guess the UI updates the state of the application by showing the user a message on whether they got the correct guess, incorrect guess and to try again, or if they lost.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
