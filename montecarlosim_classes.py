import numpy as np
import pandas as pd
import random

class die:
    #a die class with N sides/faces and W weights that can be rolled to select a face
    #Normally, dice and coins are “fair,” meaning that the each side has an equal weight. 
    #An unfair die is one where the weights are unequal.
    #Each side contains a unique symbol- Symbols may be all alphabetic or all numeric.
    #The die has one behavior, which is to be rolled one or more times.
    
    def __init__(self, faces):
        #initializer that takes an array of faces, then weights to 1, and saves into a private dataframe
        self.faces=np.array(faces)
        #raises an error if not a numpy array
        if not isinstance(faces, np.array):
            raise TypeError ("Error: not a numpy array!")
        self._faces_weights=pd.DataFrame(data = faces, columns = ['Faces'], index = range(len(faces)))
        self._faces_weights['Weights'] = np.array([1 for i in range(len(faces))])
        #raises an error if not a numpy array
        if not isinstance(faces, np.array):
            raise TypeError ("Error: not a numpy array!")
    
    def _check_unique(self, faces):
        #checks uniqueness of values and raises a ValueError if not
        seen = set()
        for item in seen:
            if item in seen:
                return False
                raise ValueError ("Value already seen!")
            seen.add(item)
        return True
    
    def change_weight(self, faces, new_weight):
        #weight can be changed after object is created
        if not (faces in list(self._faces_weights['Faces'])):
            return ValueError ("Face DNE in the list!")
        else:
            self._faces_weights.loc[self._faces_weights['Faces'] == faces, 'Weights'] = float(new_weight)
    def rolls(self, rolls=1):
        #The die has one behavior, which is to be rolled one or more times
        #Takes a parameter of how many times the die is to be rolled and defaults to 1
        rolled_results = self._faces_weights.sample(n = rolls, weights = 'Weights', replace = True)
        return list(rolled_results['Faces'])
    
    def show_me_die(self):
        #Returns a copy of the private die data frame
        return self._faces_weights

class game:
    #A game consists of rolling of one or more similar dice (Die objects) one or more times.
    #By similar dice, we mean that each die in a given game has the same number of sides and associated faces, but each may have its own weights.
    #Each game is initialized with a Python list that contains one or more dice.
    #Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.
    #Game objects only keep the results of their most recent play.
    
    def __init__(self, die_choice):
        self.die_choice = die_choice
    
    def play(self, rolls):
        self._played = pd.DataFrame()
        self.rolls = rolls
        Random_Dice = 0
        for die in self.die_choice:
            dice_results = die.rolls(rolls=rolls)
            Random_Dice += 1
            series = pd.Series(dice_results, name = f'Die{Random_Dice}')
            self._played = pd.concat([self._played, series], axis = 1)
        self._played['Roll'] = self._played.index + 1
        self._played = self._played.set_index('Roll')
        
    def show_play(self, form = 'wide'):
        #A method to show the user the results of the most recent play.
        #This method just returns a copy of the private play data frame to the user.
        #Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.
        #The narrow form will have a MultiIndex, comprising the roll number and the die number (in that order), 
        #and a single column with the outcomes (i.e. the face rolled).
        #This method should raise a ValueError if the user passes an invalid option for narrow or wide.
        self.form = form
        if not (form == 'wide' or form == 'narrow'):
            raise ValueError("INVALID: Input MUST be wide or narrow!") 
        elif form == 'wide':
            return self._played
        elif form == 'narrow':
            return self._played.stack().to_frame('Face')    

class analyzer:
    #Takes the results of a single game and computes various descriptive statistical properties about it
    def __init__(self, game):
        self._game_ = game
        self.die_dtype = type(game.die_choice[0])
        self.jackpots = 0
        self.counts_df = pd.DataFrame()

    def jackpots(self):
        #Jackpot method: a result in which all faces are the same, e.g. all ones for a six-sided die.
        #Computes how many times the game resulted in a jackpot.
        #Returns an integer for the number of jackpots.
        self.jackpots_df = pd.DataFrame()
        for i in range(1, self._game_.show_play().T.shape[1]+1):
            if ((len(set(self._game_.show_play().loc[[i]].values[0].flatten())))==1):
                temp = self._game_.show_play().loc[[i]]
                self.jackpots_df = pd.concat([self.jackpots_df, temp], axis=0)
        self.jackpots = self.jackpots_df.shape[0]
        return self.jackpots
    
    def face_count(self):    
        #facecount method to compute how many times a given face is rolled in each event
        #The data frame has an index of the roll number, face values as columns, and count values in the cells (wide format)
        self.face_count = self._game_.show_play().apply(lambda x: x.value_counts(), axis = 1).fillna(int(0))
        self.counts_df = self.face_count
        self.counts_df.index.name = 'Roll ID'
        self.counts_df.columns.name = "Die Face Shown"
        return self.counts_df
    
    def combo_count(self):
        #Computes the distinct combinations of faces rolled, along with their counts.
        #Combinations are order-independent and may contain repetitions.
        #Returns a data frame of results that should have a MultiIndex of distinct combinations and a column for the associated counts
        self.combo_df = pd.DataFrame()
        self.combo = self._game_._played.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Count')
        self.combo_df = self.combo.sort_values(by='Count')
        self.combo_df.index.names = ["Face"+str(i) for i in range(1, len(self._game_.die_choice)+1)]
        return(self.combo_df)
    
    def permute_count(self):
        #Computes the distinct permutations of faces rolled, along with their counts.
        #Permutations are order-dependent and may contain repetitions.
        #Returns a data frame of results that should have a MultiIndex of distinct permutations and a column for the associated counts
        self.permute_df = pd.DataFrame()
        self.permute = self._game_._played.apply(lambda x: pd.Series(sorted(x)), 1).value_counts_distinct().to_frame('Count')
        self.permute_df = self.combo.sort_values(by='Count')
        self.permute_df.index.names = ["Face"+str(i) for i in range(1, len(self._game_.die_choice)+1)]
        return(self.permute_df) 
        