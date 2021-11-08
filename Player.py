# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:02:53 2021

@author: Melody Jansen, s1053601
"""

class Player(object):
    """
    Class to represent a player
    
    Methods
    -------
    ___str___():
        Returns player object as string
    set_name():
        Sets name for player
    """
    
    def __init__(self):
        """
        Constructs player object and calls set name function for player

        """
        self.set_name()
    
    def __str__(self):
        """
        Returns player object as string

        """
        return self.name
    
    
    def set_name(self):
        """
        Sets name for player

        """
        self.name = input("So, first off all: what is your name? Enter here: ")
        