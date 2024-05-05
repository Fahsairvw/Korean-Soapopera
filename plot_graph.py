import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")

df = pd.read_csv('top100_kdrama.csv')
top_genre_df = df.copy()
top_genre = ['Action', 'Comedy', 'Thriller', 'Life', 'Drama', 'Melodrama']
top_genre_df = top_genre_df[(top_genre_df['Year'] >= 2015) & (top_genre_df['Genre'].isin(top_genre))]
numerical_values = ['Year', 'No of Episode', 'Duration(minute)', 'Rating']


def descriptive():
    num = ['No of Episode', 'Duration(minute)', 'Rating']
    info = df[num].describe()
    return info


class Storytelling:
    def __init__(self):
        self.data = top_genre_df
        self.year_rating = self.data.groupby('Year')['Rating'].mean()

    def first_graph(self):
        figure, ax = plt.subplots(figsize=(6, 6))
        self.data.Rating.hist(color='hotpink')
        ax.set_title('Distribution of Rating', color='blueviolet')
        return figure
    def second_graph(self):
        figure, ax = plt.subplots(figsize=(6, 6))
        sns.boxplot(x='Rating', y='Genre', data=self.data, color='aqua')
        ax.set_title('Range of the rating display by each genre', color='cornflowerblue')
        return figure

    def third_graph(self):
        figure, ax = plt.subplots(figsize=(6, 6))
        ax.plot(self.year_rating.index, self.year_rating, 'skyblue')
        ax.set_title('Rating changing through year 2015 to 2023', color='violet')
        return figure


class WhateverGraph:
    def __init__(self):
        self.numerical = top_genre_df.copy()
        self.num = self.numerical.select_dtypes(include=['int64', 'float64'])

    def pie(self):

        rating_genre = top_genre_df.groupby(['Genre']).Rating.mean()
        fig, ax = plt.subplots(figsize=(7, 6))
        slices, text, number = ax.pie(rating_genre, labels=rating_genre.index, startangle=90,
                                      counterclock=False, autopct='%1.1f%%')

        """Setting the title and legend"""
        ax.set_title('Proportion of rating')
        ax.legend(slices, rating_genre.index, title='genre', bbox_to_anchor=(1, 1))

        return fig

    def heat_map(self):
        figure, ax = plt.subplots(figsize=(7, 6))
        sns.heatmap(self.num.corr(), square=True, cbar=False, linewidths=0.25,
                    linecolor=(0, 0, 0), cmap=sns.color_palette("coolwarm"),
                    annot=True)
        return figure

    def scatter_plot(self):
        figure, ax = plt.subplots(figsize=(7, 6))
        sns.regplot(x='Rating', y='Duration(minute)', data=top_genre_df, ax=ax)
        return figure

    def histogram(self, attribute):
        figure = Figure(figsize=(7, 6))
        ax = figure.subplots()
        ax.hist(self.numerical[attribute], color='hotpink', bins=10)
        ax.set_title(f'Histogram of {attribute}')
        return figure





