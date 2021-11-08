# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:01:16 2021

@author: Melody Jansen, s1053601
"""

import Song
import time
import re

class SongQuest(object):
    """
    Class to represent a Song quest
    
    Methods
    -------
    randomized_song():
        Sets amount of points and chooses random song
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
    choose_lyrics():
        Asks player amount of wanted chars until input is valid
    get_lyrics(amount):
        Gets requested lyrics and subtracts cost of points
    give_up():
        Ends current round, sets total of points obtained in current round to 0
    song_options(option):
        Routes to command requested by player
    get_songpoints():
        Returns current amount of points obtained this round
  
    """
    
    def randomized_song(self):
        """
        Sets amount of points and chooses random song

        Returns
        -------
        None.

        """
        self.songpoints = 1000
        print("")
        song = Song.Song()
        self.song = song
        time.sleep(2)
        to_be_guessed = str(self.song).split(" ")
        
        # print title with only stars (*)
        print("SONG TO BE GUESSED: ", end="")
        for words in to_be_guessed:
            for chars in words:
                print("*", end="")
            print(" ", end="")
        print("")
        time.sleep(2)
        
        # print free hint 
        self.lyrics = self.song.get_lyrics()
        print("The first fifty characters of the song are:", end="")
        print(str(self.lyrics[0:101]).upper())
        self.index = 101
        time.sleep(2)
        
        # let player choose what's next
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
            self.song_options(option)
        
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
        clean_guess = re.sub(r'[^a-z]+', r'', guess)
        answer = str(self.song).lower()
        clean_answer = re.sub(r'[^a-z]+', r'', answer)
        if clean_guess == clean_answer:
            print("YES! That is correct! {0} by {1}, it is SUCH a good song.".format(self.song, str(self.song.get_artist())))
        else:
            print("That is... incorrect! A total of 400 points will be deducted.")
            self.songpoints -= 400
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
        print("THE MENU CARD FOR YOUR SONG HINT POSSIBILITIES:")
        print("1. Get more of the song lyrics: -4 points per character")
        print("2. Get the year the song was released: -200 points")
        print("3. Get the length of the song in minutes: -200 points")
        print("4. Get the artist: -300 points")
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
        assert choice > 0 and choice < 5
        
        if choice == 1:
            self.choose_lyrics()
        elif choice == 2:
            print(self.song.get_release())
            self.songpoints -= 200
        elif choice == 3:
            print(self.song.get_length())
            self.songpoints -= 200
        elif choice == 4:
            print(self.song.get_artist())
            self.songpoints -= 300
            
    def choose_lyrics(self):
        """
        Asks player amount of wanted chars until input is valid

        Returns
        -------
        None.

        """
        
        try:
            amount = int(input("How many characters of the lyrics do you want? Max is 300. Your choice: "))
            self.get_lyrics(amount)
            
        # if input is not a number
        except ValueError:
            print("That doesn't seem like it even is a number. Try again.")
            self.choose_lyrics()
            
        # if input is not a valid number
        except AssertionError:
            print("Hm. That doesn't seem to work. If the value you entered is between 0 and 301, maybe the song doesn't have that many chars left. Try a smaller number")
            self.choose_lyrics()
            
    def get_lyrics(self, amount):
        """
        Gets requested lyrics and subtracts cost of points

        Parameters
        ----------
        amount : int
            amount of characters in lyrics requested.

        Returns
        -------
        None.

        """
        assert amount > 0 and amount < 301
        assert amount + self.index < len(self.lyrics)
        
        print(str(self.lyrics[1:self.index+amount]).upper())
        self.index += amount
        self.songpoints -= amount * 4
        
        
    def give_up(self):
        """
        Ends current round, sets total of points obtained in current round to 0

        Returns
        -------
        None.

        """
        print("I thought failure was never an option, but here we go.")
        print("The song you had to guess was {0}. Come on, haven't you heard it?".format(self.song))
        print("Just an advice: go to youtube and look up {0} by {1}. You have got to know this song, come on!".format(self.song, str(self.song.get_artist())))
        self.songpoints = 0      
        
    def song_options(self, option):
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
            
    def get_songpoints(self):
        """
        Returns current amount of points obtained this round
        """
        return self.songpoints
    