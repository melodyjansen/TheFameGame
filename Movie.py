# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:44:18 2021

@author: Melody Jansen, s1053601
"""

import pandas as pd
import random

class Movie(object):
    """
    Class to represent a movie
    
    Methods
    -------
    ___str___():
        Returns movie object as string
    get_overview():
        Returns overview of movieplot
    get_release():
        Returns date of release of movie
    get_genre():
        Returns main genre of movie
    get_length():
        Returns length of movie in minutes
    get_producer():
        Returns producer(s) of the movie
    get_tagline():
        Returns tagline of the movie
    """
    
    def __init__(self):
        """
        Constructs movie object, imports and cleans movie database

        Returns
        -------
        None.

        """
        movie_data = pd.read_csv("MovieData.csv", low_memory=False)
        movie_data = movie_data[(movie_data['vote_count'] > 2000)]
        del movie_data["popularity"]
        self.movie_data = movie_data
        movie_row = random.randint(0,361)
        random_movie = movie_data.iloc[movie_row, 19]
        self.random_movie = random_movie
        self.movie_row = movie_row
    
    def __str__(self):
        """
        Returns movie title as string
        """
        return self.random_movie
    
    def get_overview(self):
        """
        Gathers overview from dataset and replaces occurences of the exact movie title with a string

        Returns
        -------
        overview : str
            movie description.

        """
        overview = self.movie_data.iloc[self.movie_row, 9]
        if (overview.find(self.random_movie) != -1):
            overview = overview.replace(self.random_movie, "***")
        return overview
    
    def get_release(self):
        """
        Gathers releasedata from database

        Returns
        -------
        releasedate : str
            date the movie to be guessed was released.

        """
        releasedate = self.movie_data.iloc[self.movie_row, 13] 
        return releasedate
    
    def get_genre(self):
        """
        Gathers genre from dataset

        Returns
        -------
        genre : str
            genre of movie to be guessed.

        """
        genres_data = self.movie_data.iloc[self.movie_row, 3]
        genre = genres_data.split("'")
        return genre[5]
    
    def get_length(self):
        """
        Gathers runtime in minutes from database

        Returns
        -------
        runtime : str
            length of movie to be guessed in minutes.

        """
        runtime = str(self.movie_data.iloc[self.movie_row, 15]) + " minutes"
        return runtime
    
    def get_producer(self):
        """
        Gathers producers from database

        Returns
        -------
        producer : str
            production company that produced the to be guessed movie

        """
        producer_data = self.movie_data.iloc[self.movie_row, 11]
        producer = producer_data.split("'")
        return producer[3]+ " AND " + producer[9]
    
    def get_tagline(self):
        tagline = self.movie_data.iloc[self.movie_row, 18]
        return tagline
