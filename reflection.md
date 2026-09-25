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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Use Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - For the bug that I found *When you change the difficulty in the sidenav, it does not update the low and high values in the blue box*, I used the LLM to generate a unit test in the `test_game_logic.py` file since I did not know how to use the pytest framework to test the UI state changes. Now I have a better idea on how to test!
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decided whether a bug was fixed when my tests pass successfully and looking at the UI where I tested what I proposed in the unit test
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
