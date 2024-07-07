import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

def categorical_plot(data, columns):
   fig = plt.figure()

   for col in columns[1:-1]:  
    group_data = data.groupby(col, axis=0).sum()

    group_data['Flights'].plot(kind='pie',figsize=(5, 6),
                                autopct='%1.1f%%', # add in percentages
                                startangle=90,     # start angle 90° (Africa)
                                shadow=True,       # add shadow      
                                )
    plt.title(f'Pie Chart for {col}')
    plt.show()

def numerical_plot(df, y_colums):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date_year'] = df['Date'].dt.year
    x_col = 'PayloadMass'

    y_colums = ['Orbit']
    for y_col in y_colums:
        plt.figure(figsize=(10, 5))
        # Plot Scatter 
        plt.scatter(df[x_col], df[y_col])
        plt.title(f'Scatter Plot')
        plt.ylabel(f'Number of {y_col}')
        plt.xlabel(x_col)
        plt.show()
        # Plot Histogram
        plt.hist(df[y_col])
        plt.title(f'Distribution of {y_col}')
        plt.ylabel(f'Count number of {y_col}')
        plt.xlabel(y_col)
        plt.show()
        # Plot Boxplot
        sns.boxplot(y=df[y_col])
        plt.title(f'Box Plot')
        plt.ylabel(f'Count number of {y_col}')
        plt.xlabel(y_col)
        plt.show()


def main():
    data = pd.read_csv("dataset_collected.csv")
    df = pd.DataFrame(data)

    # list the data types for each column
    df.dtypes
    # Descreptive 
    df.describe()

    # Then, group columns into Numerial and Gategoriacal
    cat_colums = ['Orbit','BoosterVersion','LaunchSite','Serial']
    num_colums = ['ReusedCount','Block','PayloadMass','Date']

    # Find the correlation between column
    corr = df[cat_colums].corr()


    # --------- CONTINUOUS VARIABLE ----------------
    # Visualize Continuous Variable
    numerical_plot(df, num_colums[:-1])


    # --------- CATEGORICAL VARIABLE ---------------
    # Visualize Categorial Variable 
    categorical_plot(df, cat_colums)



if __name__ == '__main__':
  main()