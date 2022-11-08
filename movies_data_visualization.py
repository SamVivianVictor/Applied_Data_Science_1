import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""This function draws two line plots one corresponding to movie ratings 
   and the other corresponding to movie runtime."""
def line_plot(data):
    movie_id = data.iloc[:, 0]
    ratings = data.iloc[:, 8]
    runtime = data.iloc[:, 7]
    plt.figure()
    """This plot plots the Movie ratings on Y axis and Movie IDs on X axis"""
    plt.plot(movie_id.tolist(), ratings.tolist(), label='Movie Ratings')
    """This plot plots the Movie runtime values on Y axis and Movie IDs on 
       X axis"""
    plt.plot(movie_id.tolist(), runtime.tolist(), label='Movie Runtime')
    plt.xlabel('Movie Id')
    plt.title('Line plot showing movie ratings and movie runtime')
    plt.xlim(1, 20)
    plt.ylim(1, 175)
    plt.legend()
    plt.show()
    
"""This function draws a histogram of movie runtime values."""
def runtime_hist_plot(data):
    runtime = data.iloc[:, 7]
    plt.figure()
    plt.hist(runtime, density=True, bins=50, label='Movie Runtime')
    plt.xlabel('Movie Runtime')
    plt.ylabel('Probability')
    plt.title('Histogram plot showing movie runtime')
    plt.legend()
    plt.show()
    
"""This function draws a pie chart of different movie genres as per their
   frequencies."""
def genre_pie_plot(data):
    """This variable stores the probabilitis of the frequencies of different
       movie genres. It is of type Pandas.Series"""
    probability_of_each_genre = data.iloc[:, 6].value_counts(normalize=True)
    plt.figure()
    """The variable 'labels' stores the names of all Genres"""
    labels = probability_of_each_genre.index
    plt.pie(probability_of_each_genre, labels=labels)
    """This variable stores the genres with their percentage of occurances"""
    labels_with_size = [f'{l}, {p:0.1f}%' for l, p in 
                        zip(labels, probability_of_each_genre*100)]
    """Legend is placed outside the pie chart so that they don't overlap"""
    plt.legend(loc=(1.2, 0), labels=labels_with_size)
    plt.title('Pie chart showing frequencies of \n different movie genres')
    plt.show()

"""This block of code reads the 'movies.csv' dataset and three function 
   calls are made, each corresponding to each plot."""
data = pd.read_csv('movies.csv')
line_plot(data)
runtime_hist_plot(data)
genre_pie_plot(data)