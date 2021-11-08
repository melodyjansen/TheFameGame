# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:07:00 2021

@author: Melody Jansen, s1053601
"""

import time

class Host(object):
    """
    Class to represent the game show host
    
    Methods
    -------
    explain():
        Prints timed explanatory statements
    """
    
    
    def __init__(self):
        """
        Constructs Host object and prints timed welcome statements

        Returns
        -------
        None.

        """
        print("Hello everybody, and welcome to your favorite game show.")
        time.sleep(2)
        print("Here we are again with the FAME GAME!")
        time.sleep(2)
        print("Just a short warning; viewer discretion is advised. Some of the songs being guessed here may contain explicit language.")
        time.sleep(2)
        print("I will be your host for today, my name is Spyder.")
        time.sleep(2)
        print("But now I am wondering.. Who will be our brave contestant today?")
        time.sleep(2)
        print("Let us get to know you!")
        time.sleep(2)
        print("...")
        
    def explain(self):
        """
        Prints timed explanatory statements

        Returns
        -------
        None.

        """
        time.sleep(2)
        print("We will give you five options to gain points.")
        time.sleep(2)
        print("The first option, you have to guess a movie.")
        time.sleep(2)
        print("The last four will be songs.")
        time.sleep(2)
        print("You can get a maximum of a 1000 points for each correct guess.")
        time.sleep(2)
        print("But-- each time you need a hint, a number of points will be deducted.")
        time.sleep(2)
        print("And for every wrong guess-- 400(!) points will be deducted.")
        time.sleep(2)
        print("Let's just start the game! You'll understand it as we go along!")
        time.sleep(2)