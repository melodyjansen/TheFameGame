# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:20:40 2021

@author: Melody Jansen, s1053601
"""

import Movie
import time
import re

class MovieQuest(object):
    """
    Class to represent a Movie quest
    
    Methods
    -------
    randomized_movie():
        Sets amount of points and chooses random movie
    choose():
        Asks player to choose what they want to do next until input given is valid
    take_guess():
        Asks player for their guess
    hint_options():
        Print all possible hint options
    choose_hint():
        Asks what hint the player wants until given input is valid
    hint_option(choice):
        Obtains correct hint wanted by player and subtracts cost of points
    give_up():
        Ends current round, sets total of points obtained in current round to 0
    movie_options(option):
        Routes to command requested by player
    get_moviepoints():
        Returns current amount of points obtained this round
  
    """
    
    def randomized_movie(self):
        """
        Sets amount of points and chooses random movie

        Returns
        -------
        None.

        """
        self.moviepoints = 1000
        print("")
        movie = Movie.Movie()
        self.movie = movie
        time.sleep(2)
        
        # print title with only stars (*)
        to_be_guessed = str(self.movie).split(" ")
        print("MOVIE TO BE GUESSED: ", end="")
        for words in to_be_guessed:
            for chars in words:
                print("*", end="")
            print(" ", end="")
        print("")
        
        # print free hint 
        if self.movie.get_tagline() != "NaN":
            print("The TAGLINE of this movie is:")
            print(self.movie.get_tagline())
        else:
            print("We will give you the first sentence of the overview for this movie.")
            overview = self.movie.get_overview()
            pre_overview = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', overview)
            print(pre_overview)
        time.sleep(2)
        
        # have player choose what's next
        self.choose()
        
    def choose(self):
        """
        Asks player to choose what they want to do next until input given is valid

        Returns
        -------
        None.

        """
        try:
            option = int(input("Enter 1 to take your guess. Enter 2 for a hint. Enter 3 to give up and move on with 0 points. Your choice: "))
            self.movie_options(option)
            
        # if input is not a number
        except ValueError:
            print("That doesn't seem like it even is a number. Try again.")
            self.choose()
            
        # if input is not a valid number
        except AssertionError:
            print("Looks like the value you entered is not an option. Try again.")
            self.choose()
                        
    def take_guess(self):
        """
        Asks player for their guess

        Returns
        -------
        None.

        """
        guess = str(input("Alright! Enter your guess: ")).lower()
        
        # rid guess and answer of symbols and spaces to minimize unnecessary errors
        clean_guess = re.sub(r'[^a-z]+', r'', guess)
        answer = str(self.movie).lower()
        clean_answer = re.sub(r'[^a-z]+', r'', answer)
        
        # check if guess and answer are the same
        if clean_guess == clean_answer:
            print("That is 100% correct! Very good job!")
        else:
            print("That is... incorrect! A total of 400 points will be deducted.")
            self.moviepoints -= 400
            time.sleep(2)
            time.sleep(2)
            self.choose()
        
    def hint_options(self):
        """
        Print all possible hint options

        Returns
        -------
        None.

        """
        time.sleep(2)
        print(" ")
        print("THE MENU CARD FOR YOUR MOVIE HINT POSSIBILITIES:")
        print("1. Get an overview of your movie: -400 points")
        print("2. Get the date the movie was released: -200 points")
        print("3. Get the movie its main genre: -200 points")
        print("4. Get the length of the movie in minutes: -200 points")
        print("5. Get the producer(s) of the movie: -100 points")
        self.choose_hint()
        self.choose()
        
    def choose_hint(self):
        """
        Asks what hint the player wants until given input is valid

        Returns
        -------
        None.

        """
        try:
            choice = int(input("Enter the number assigned to the hint of your choice: "))
            self.hint_option(choice)
            
        # if input is not a number
        except ValueError:
            print("That doesn't seem like it even is a number. Try again.")
            self.choose_hint()
        
        # if input is not a valid number
        except AssertionError:
            print("Looks like the value you entered is not an option. Try again.")
            self.choose_hint()         
            
    def hint_option(self, choice):
        """
        Obtains correct hint wanted by player and subtracts cost of points

        Parameters
        ----------
        choice : int
            Number assigned to hint of player's choice.

        Returns
        -------
        None.

        """
        assert choice > 0 and choice < 6
        
        if choice == 1:
            print(self.movie.get_overview())
            self.moviepoints -= 400
        elif choice == 2:
            print(self.movie.get_release())
            self.moviepoints -= 200
        elif choice == 3:
            print(self.movie.get_genre())
            self.moviepoints -= 200
        elif choice == 4:
            print(self.movie.get_length())
            self.moviepoints -= 200
        elif choice == 5: 
            print(self.movie.get_producer())
            self.moviepoints -= 100    
    
    def give_up(self):
        """
        Ends current round, sets total of points obtained in current round to 0

        Returns
        -------
        None.

        """
        print("I thought failure was never an option, but here we go.")
        print("The movie you had to guess was {0}. Come on, haven't you seen it?".format(self.movie))
        self.moviepoints = 0      
        
    def movie_options(self, option):
        """
        Routes to command requested by player

        Parameters
        ----------
        option : int
            Number assigned to option requested by player.

        Returns
        -------
        None.

        """
        assert option > 0 and option < 4
        
        if option == 1:
            self.take_guess()
        elif option == 2:
            self.hint_options()
        elif option == 3:
            self.give_up() 
            
    def get_moviepoints(self):
        """
        Returns current amount of points obtained this round
        """
        return self.moviepoints
    