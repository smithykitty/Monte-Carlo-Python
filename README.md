# DS5100-cmj4ec
Metadata:
Final Project (Monte Carlo Simulator)
DS5100
Catherine M Smith
cmj4ec

Synopsis:
The Monte Carlo Sim Package is a Python package with three classes: Die, Game, and Analyzer. 
Continue reading below for descriptions and demonstration code.

API Description - Classes and attributes:
The Die Class:
A die class with N sides/faces and W weights that can be rolled to select a side/face.
Normally, dice and coins are “fair,” meaning that the each side has an equal weight. 
An unfair die is one where the weights are unequal.
Each side contains a unique symbol- Symbols may be all alphabetic or all numeric.
The die has one behavior, which is to be rolled one or more times.

The Game Class:
A game consists of rolling of one or more similar dice (Die objects) one or more times.
By similar dice, we mean that each die in a given game has the same number of sides and associated faces, but each may have its own weights.
Each game is initialized with a Python list that contains one or more dice.
Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.
Game objects only keep the results of their most recent play.

The Analyzer Class:
Takes the results of a single game and computes various descriptive statistical properties about it.
Includes a Jackpot method: a result in which all faces are the same, e.g. all ones for a six-sided die.
Computes how many times the game resulted in a jackpot; returns an integer for the number of jackpots.
The facecount method computes how many times a given face is rolled in each event.
Note the data frame has an index of the roll number, face values as columns, and count values in the cells.
The combo count and permute count also compute the distinct combinations rolled and return a dataframe of results.

Install:
!pip install .
Importing:
from montecarlosim import Die, Game, Analyzer
Creating dice:
Create the die object called myDie:
myDie = Die(['face1', 'face2', 'face3'])
Change the weight of 'face1':
myDie.change_weight('face1', 3)
Show the faces and weights of myDie:
myDie.show_die()
Roll myDie five times:
myDie.rolls(5)

Play:
Create the game object myGame:
myGame = Game([Die([1,2,3]), Die([1,2,3]), Die([1,2,3])])

Play the game using myGame, input value in the rolls parameter to specify number of times each die is to be rolled:

myGame.play(3)
Show the results of play, input either 'wide' or 'narrow' for the form parameter to specify the format of the df of results to be shown (defaults to wide).

myGame.show_play()
Analyzing games:

Make the analyzer object myAnalyzer using myGame:
myAnalyzer = Analyzer(myGame)

Return a df with counts for the occurrence of each face value per roll:
myAnalyzer.face_count()

Get how many times a jackpot occurred:
myAnalyzer.jackpot()

Get the combinations of faces rolled and their counts:
myAnalyzer.combo()

Manifest:
Files in repo:
final_project
init
montecarlosim
init.py
montecarlosim.py
montecarlosim_demo.ipynb
montecarlosim_tests.py
setup.py
test_results.txt
LICENSE
README.md