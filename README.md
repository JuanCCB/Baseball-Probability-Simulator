# Baseball-Probability-Simulator
Python scripts that estimate probabilities of winning of any team and simulate a whole baseball match.

This project allows to estimate probabilities of winning of every team in the MLB's American and National Leagues. These projections are based on discrete statistics of pitching and batting of every player during their 5 recents seasons, the main source of these statistics is Google Statcast through PyBaseball module whereas the source of every player's position is taken from https://www.baseball-reference.com/.

## MainSimulator.py

This script let simulate an entire baseball match based on every player's statistics and information of their position in the field.

![image](https://user-images.githubusercontent.com/107895120/180108143-a1feb34d-747f-4350-b002-7c8f2757304e.png)

i.e. Simulation of a baseball match between Atlanta Braves vs New York Yankees.

## MainProbability.py

This script allows to estimate the probability of winning in a match between the home and the away team. These probabilities are estimated on the logics of MainSimulator.py in silence mode that permits to simulate until 10,000 matches with that purpose.

![image](https://user-images.githubusercontent.com/107895120/180107414-1baa01fb-90b9-4f6d-bb9e-795075447ef2.png)

i.e. Probability estimation of a possible match between Atlanta Braves vs New York Yankees based on 10,000 simulations.

Results:

![image](https://user-images.githubusercontent.com/107895120/180107755-1eecd029-2dbf-4248-a8c5-e8917ac6c951.png)

This project was possible thanks to the initial contributions of Ben Ryan and James LeDoux.
