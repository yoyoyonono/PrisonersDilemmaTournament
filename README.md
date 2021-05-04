# PrisonersDilemmaTournament

This is my CS 269i class project.

Watch This Place's awesome video about iterated Prisoner's Dilemma for context! https://www.youtube.com/watch?v=BOvAbjfJ0x0

Nicky Case's "The Evolution of Trust" is also a must-see: https://ncase.me/trust/

How this works:
When you run code/prisonersDilemma.py, it will search through all .py strategy files in code/exampleStrats. Then, it will simulate Prisoner's Dilemma with every possible pairing. (There are (n choose 2) simulations.) After all simulations are done, then it will average each strategies' overall score across all its pairings. It will then produce a leaderboard of strategies based on their average performance!

Details:
| First Header  | Player A cooperates | Player A defects |
| ------------- | ------------- | ------------- |
| Player B cooperates  | A: +3, B: +3  | A: +5, B: +0  |
| Player A cooperates  | A: +0, B: +5  | A: +1, B: +1  |

Each pairing simulation runs for this many turns:
```
200-40*np.log(random.random())
```
This means each game is guaranteed to be at least 200 turns long. But then, for every turn after the 200th, there is an equal probability that the game ends. The probability is very low, so there should be no strategizing to, say, defect on the very last turn consequence-free.