import unittest
#from montecarlosim import Die, Game, Analyzer
import pandas as pd
import numpy as np
import pandas.testing as pdt
from montecarlo.montecarlosim_classes import die, game, analyzer
#Test via Unittest package containing at least one method for each method in each of the three classes 
#Each test method should verify that the target method creates an appropriate data structure
class montecarlosimTestSuite(unittest.TestCase):
    #Test Suite for Monte Carlo Simulator
    
    def test_die(self):
        #create a 6-sided die with valid sides/weight
        die = die([1,2,3,4,5,6])
        x = 1
        if x not in die.faces_weights['Weights'].values:
            raise AssertionError('Invalid Weight!')
    
    def test_check_unique(self):
        #checks uniqueness of values and raises a ValueError if not unique
        die = [a,b,c,d,e,f]
        self.assertTrue(test_check_unique(die), "FAIL: List must have unique values!")
        
        
    def test_check_unique_dupe(self):
        #test with duplicate values
        die = [1,2,2,3,4,5]
        self.assertFalse(test_check_unique_dupe(die), "FAIL: List with duplicate values!") 
        
    def test_weight_change(self):
        #change the weight of a side
        die = die([1,2,3,4,5,6])
        die.change_weight(2,3)
        expected = 3
        actual = die.show_die().loc[die.show_die()['Faces'] == 2, 'Weights'].values[0]
        self.assertEqual(expected, actual)
    
    def test_rolls(self):
        #The die has one behavior, which is to be rolled one or more times
        #Takes a parameter of how many times the die is to be rolled and defaults to 1
        die = [A,1,B,2,C,3]
        test_rolls = die(die)
        roll = test_rolls.rolls(4)
        self.assertEqual(len(roll), 4)
    
    def test_show_me_die(self):
        #Returns a copy of the private die data frame
        die = [1,2,3,4,5,6]
        test_show_me_die = Die(die)
        test_show_me_die_df = test_show_me_die_df.show_die()
        test_show_me_die_type = type(test_show_me_die_df)
        x = pd.DataFrame()
        pd_type = type(x)
        self.assertEqual(test_show_me_die_type, pd_type)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)
