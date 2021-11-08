# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:34:03 2021

@author: Melody Jansen, s1053601
"""

import Player
import Host
import MovieQuest
import SongQuest
import time
import webbrowser

class FameGame(object):
    """
    Class to represent the Fame Game
    
    Methods
    -------
    welcome():
        Creates Host and Player objects, sets amount of points to 0
    final_message():
        Prints response to amount of points achieved by player
    try_again():
        Asks if player wants to play again until input is valid
    play():
        Main game with one movie quest last four song quests in a loop
        
    """
    
    def __init__(self):
        """
        Creates FameGame object with empty array for points, starts game

        Returns
        -------
        None.

        """
        self.complete_points = []
        self.welcome()
        self.play()
        
    def welcome(self):
        """
        Creates Host and Player objects, sets amount of points to 0

        Returns
        -------
        None.

        """
        host = Host.Host()
        self.host = host
        player = Player.Player()
        self.player = player
        self.points = 0
        print("Great! Have a seat, {0}. Let me just repeat the rules of the game.".format(self.player))
        self.host.explain()
    
    def final_message(self):
        """
        Prints response to amount of points achieved by player

        Returns
        -------
        None.

        """
        
        # if amount of points achieved negative
        if self.points <= 0:
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("You uncultured swine.")
            time.sleep(2)
            print("Most likely you don't even understand the latest comment was a reference to a great, great movie.")
            time.sleep(2)
            print("It's called Toy Story.")
            time.sleep(2)
            print("You should give it a watch sometime.")
            
        # if amount of points achieved low
        if self.points <= 1000 and self.points > 0:  
            print("That did not go very well. Listen to more music! Watch more movies! Broaden your horizon.")
            time.sleep(1)
            print("These things may seem insignificant, but they are not!")    
            
        # if amount of points achieved OK
        if self.points > 1000 and self.points <= 3000:
            print("Seems like you have a pretty decent understanding of culture. You could have done better, but this was alright!")
        if self.points > 3000 and self.points <= 4000:
            print("Whoa, good job there {0}! Very well done.".format(self.player))
        
        # if amount of points achieved is almost max
        if self.points > 4000:
            print("....")
            time.sleep(2)
            print("How?")
            time.sleep(2)
            print("That was amazing!")
            time.sleep(2)
            print("If there was a prize, you would have won it.")
            time.sleep(2)
            print("Congratulations!")
            
    def try_again(self):
        """
        Asks if player wants to play again until input is valid

        Returns
        -------
        None.

        """
        answer = input("I'm sure though that you can do better, still! Want to try again? Enter yes or no: ").lower()
        while len(answer) < 1 or not answer[0] == 'y' and not answer[0] =='n':
            answer = input("That input isn't recognized. Choose yes or no please: ").lower()
        if answer[0] == 'n':
            print("Goodbye!")
        elif answer[0] == 'y':
            print("Nice! Good luck.")
            self.points = 0
            self.play()
        
            
    def play(self):
        """
        Main game with one movie quest last four song quests in a loop

        Returns
        -------
        None.

        """
        # round 1
        print("_____________________________________")
        print(" ")
        print("______ROUND 1: GUESS THE MOVIE_______")
        print("_____________________________________")
        print("_____________________________________")
        movieQuest = MovieQuest.MovieQuest()
        self.movieQuest = movieQuest
        self.movieQuest.randomized_movie()
        self.points += movieQuest.get_moviepoints()
        print("Current amount of points: {}".format(self.points))
        time.sleep(3)
        
        # round 2 - 5
        for i in range(4):
            print("_____________________________________")
            print(" ")
            print("______ROUND {0}: GUESS THE SONG________".format(i+2))
            print("_____________________________________")
            print("_____________________________________")
            songQuest = SongQuest.SongQuest()
            self.songQuest = songQuest
            self.songQuest.randomized_song()
            self.points += songQuest.get_songpoints()
            print("Current amount of points: {}".format(self.points))
            time.sleep(3) 
            
        # finalize play
        self.complete_points.append(self.points)
        print("")
        print("That was the last round!")
        
        # check if earlier plays exist and if player scored better
        if len(self.complete_points) > 0:
            if self.points > max(self.complete_points):
                print("Well, that's a high score, {0}! You did better than last time(s).".format(self.player))
        
        # optional extra free hint
        answer = input("You want one more free hint? For the game in general? Enter yes or no: ").lower()
        while len(answer) < 1 or not answer[0] == 'y' and not answer[0] =='n':
            answer = input("That input isn't recognized. Choose yes or no please: ").lower()
        if answer[0] == 'n':
            print("Alright! Let's talk about the way you scored. {0} points huh.".format(self.points))
        elif answer[0] == 'y':
            print("Here you go! This is the holy grail to getting at least 4000 points on the game next time.")
            webbrowser.open("https://open.spotify.com/playlist/3OEpEFU82KDwW8GhlNuyql?si=ba27732e238f43bf")
        # final words
        self.final_message()
        self.try_again()
        
        
game = FameGame()
        