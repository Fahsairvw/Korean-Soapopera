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


class Storytelling:
    def __init__(self):
        self.data = top_genre_df
        self.year_rating = self.data.groupby('Year')['Rating'].mean()

    def first_graph(self):
        ax = self.data.Rating.hist(color='hotpink')
        ax.set_title('Distribution of Rating', color='blueviolet')
        plt.show()

    def second_graph(self):
        ax = sns.boxplot(x='Rating', y='Genre', data=self.data, color='aqua')
        ax.set_title('Range of the rating display by each genre', color='cornflowerblue')
        plt.show()

    def third_graph(self):
        fig, ax = plt.subplots()
        ax.plot(self.year_rating.index, self.year_rating, 'skyblue')
        ax.set_title('Rating changing through year 2015 to 2023', color='violet')
        plt.show()


class WhateverGraph:
    def __init__(self):
        pass

    def pie(self):
        rating_genre = top_genre_df.groupby(['Genre']).Rating.mean()
        fig, ax = plt.subplots()
        slices, text, number = ax.pie(rating_genre, labels=top_genre_df['Genre'].unique(), startangle=90,
                                      counterclock=False, autopct='%1.1f%%')
        ax.set_title('Proportion of rating')
        ax.legend(slices, top_genre_df['Genre'].unique(), title='genre', bbox_to_anchor=(1, 1))

    def heat_map(self):
        pass

    def scatter_plot(self):
        pass

    def histogram(self):
        pass


if __name__ == '__main__':
    ui = WhateverGraph()
    ui.pie()
