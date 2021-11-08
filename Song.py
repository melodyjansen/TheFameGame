# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:14:23 2021

@author: Melody Jansen, s1053601
"""

import pandas as pd
import random

class Song(object):
    """
    Class to represent a song
    
    Methods
    -------
    ___str___():
        Returns song object as string
    get_artist():
        Returns artist of song
    get_release():
        Returns year of release of song
    get_lyrics():
        Returns lyrics of song
    get_length():
        Retuns length of song in minutes
    """
    
    def __init__(self):
        """
        Constructs song object, imports and cleans song database

        Returns
        -------
        None.

        """
        song_data = pd.read_csv("SongData.csv", low_memory=False)
        song_data = song_data[(song_data['popularity'] > 72)]
        self.song_data = song_data
        song_row = random.randint(0,414)
        random_song = song_data.iloc[song_row, 6]
        self.random_song = random_song
        self.song_row = song_row
        
    def __str__(self):
        """
        Returns song title as string, overrides superclass

        """
        return self.random_song
    
    def get_artist(self):
        """
        Gather artist of song from database

        Returns
        -------
        artist : str
            artist/band that sang the song.

        """
        artist = self.song_data.iloc[self.song_row, 0]
        return artist
    
    def get_release(self):
        """
        Gathers year of release from database

        Returns
        -------
        releasedate : str
            year the song to be guessed was released.

        """
        release = self.song_data.iloc[self.song_row, 4]
        return release
    
    def get_lyrics(self):
        """
        Gathers lyrics from database

        Returns
        -------
        lyrics : str
            lyrics of song to be guessed.

        """
        lyrics = self.song_data.iloc[self.song_row, 8]
        return lyrics
    
    def get_length(self):
        """
        Gathers length in minutes from database, overrides superclass

        Returns
        -------
        length : str
            length of song to be guessed in minutes.

        """
        length = str(self.song_data.iloc[self.song_row, 24])
        return length + " minutes"        