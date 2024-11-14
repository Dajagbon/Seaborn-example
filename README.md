# Assignment-9-Seaborn
# Project Title: Data Visualization with Seaborn

## Purpose
This project aims to demonstrate various data visualization techniques using the Seaborn library in Python. The project includes examples of relational, distributional, and categorical plots to analyze and visualize datasets effectively. The primary datasets used in this project are a custom exercise dataset and the built-in planets dataset from Seaborn.

## Class Design and Implementation
This project does not use custom classes; instead, it focuses on using functions and Seaborn's plotting capabilities to create visualizations. Below is an explanation of the key components and methods used in the project.

### Key Components

1. **Exercise Data Visualization**:
    - **Heatmap**: Visualizes pulse data by exercise type and time.
    - **Categorical Plot**: Shows pulse values by diet type and exercise type.
    - 
**Briefly explain what conclusions can be drawn from the data given to the elementary school students**
The more intense the exercise (like running), the faster your heart beats to pump blood and oxygen to your muscles. Understanding how exercise affects your heart rate can help you understand the importance of staying active and healthy. We noticed that the type of diet can also affect your heart rate. For example, eating a low-fat or no-fat diet can change how your heart responds to exercise. Both diets showed that running increased the pulse the most, but the pulse was slightly higher for the no-fat diet when running.

2. **Planets Data Visualization**:
    - **Scatter Plot**: Shows the relationship between distance and orbital period.
    - **Line Plot**: Shows the relationship between the year of discovery and planet mass.
    - **Histogram**: Shows the distribution of orbital periods.
    - **Box Plot**: Shows the distribution of planet mass by detection method.
    - **Bar Plot**: Shows the number of planets discovered yearly.
    - **Violin Plot**: Shows the average orbital period for each detection method.
    - 
**Provide a brief explanation about which graph(s) you feel best to demonstrate something notable about the data and how it is illustrated.**
The scatter and bar plots best demonstrate something notable about the data. The scatter plot shows the relationship between distance and orbital period. The scatter graph highlights how different detection methods cluster around specific ranges of distance and orbital periods. For example, methods like Radial Velocity and Transit show a concentration at shorter distances and orbital periods. Also, each detection method is represented by a distinct color, making it easy to differentiate and compare their distributions. Furthermore, the bar plot shows the number of planets discovered yearly. The graph shows a marked increase in the number of planets discovered per year from 1989 to 2014, emphasizing how technological advancements and focused efforts in astronomy have paid off. Finally, each bar represents the count of planets discovered in a given year, making it easy to compare year-over-year changes.

### Methods and Attributes

#### Exercise Data Visualization
- **Heatmap**:
    - 

plt.figure(figsize=(10, 8))

: Sets the figure size.
    - 

sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')

: Creates a heatmap with annotations and a coolwarm color map.
    - 

plt.title('Heatmap of Pulse Data by Exercise Type and Time')

: Sets the title of the heatmap.
    - 

plt.xlabel('Time')

: Sets the x-axis label.
    - 

plt.ylabel('Exercise Type')

: Sets the y-axis label.
    - 

plt.show()

: Displays the plot.

- **Categorical Plot**:
    - 

sns.catplot(x='diet', y='Pulse', hue='kind', kind='bar', data=pulse_data, height=6, aspect=2)

: Creates a bar plot with diet on the x-axis, pulse on the y-axis, and different hues for exercise types.
    - 

plt.title('Pulse Values by Diet Type and Exercise Type', fontsize=8, pad=10)

: Sets the title of the plot with font size and padding.
    - 

plt.xlabel('Diet Type')

: Sets the x-axis label.
    - 

plt.ylabel('Pulse')

: Sets the y-axis label.
    - 

plt.legend(title='Exercise Type')

: Sets the legend title.
    - 

plt.show()

: Displays the plot.

#### Planets Data Visualization
- **Scatter Plot**:
    - 

plt.figure(figsize=(10, 6))

: Sets the figure size.
    - 

sns.scatterplot(data=planets, x='distance', y='orbital_period', hue='method')

: Creates a scatter plot with distance on the x-axis, orbital period on the y-axis, and different hues for detection methods.
    - 

plt.title('Relationship between Distance and Orbital Period')

: Sets the title of the scatter plot.
    - 

plt.xlabel('Distance (AU)')

: Sets the x-axis label.
    - 

plt.ylabel('Orbital Period (days)')

: Sets the y-axis label.
    - 

plt.legend(title='Detection Method')

: Sets the legend title.
    - 

plt.show()

: Displays the plot.

- **Line Plot**:
    - 

plt.figure(figsize=(10, 6))

: Sets the figure size.
    - 

sns.lineplot(data=planets, x='year', y='mass', hue='method', marker='o')

: Creates a line plot with year on the x-axis, mass on the y-axis, and different hues for detection methods.
    - 

plt.title('Yearly Discovery of Planet Mass')

: Sets the title of the line plot.
    - 

plt.xlabel('Year')

: Sets the x-axis label.
    - 

plt.ylabel('Planet Mass (Jupiter Masses)')

: Sets the y-axis label.
    - 

plt.legend(title='Detection Method')

: Sets the legend title.
    - 

plt.show()

: Displays the plot.

- **Histogram**:
    - 

plt.figure(figsize=(10, 6))

: Sets the figure size.
    - 

sns.histplot(data=planets, x='orbital_period', kde=True)

: Creates a histogram with orbital period on the x-axis and a kernel density estimate.
    - 

plt.title('Distribution of Orbital Period')

: Sets the title of the histogram.
    - 

plt.xlabel('Orbital Period (days)')

: Sets the x-axis label.
    - 

plt.ylabel('Frequency')

: Sets the y-axis label.
    - 

plt.show()

: Displays the plot.

- **Box Plot**:
    - 

plt.figure(figsize=(10, 6))

: Sets the figure size.
    - 

sns.boxplot(data=planets, x='method', y='mass')

: Creates a box plot with detection method on the x-axis and mass on the y-axis.
    - 

plt.title('Distribution of Planet Mass by Detection Method')

: Sets the title of the box plot.
    - 

plt.xlabel('Detection Method')

: Sets the x-axis label.
    - 

plt.ylabel('Planet Mass (Jupiter Masses)')

: Sets the y-axis label.
    - 

plt.xticks(rotation=90)

: Rotates the x-axis labels by 90 degrees.
    - 

plt.show()

: Displays the plot.

- **Count Plot**:
    - 

plt.figure(figsize=(10, 6))

: Sets the figure size.
    - 

sns.countplot(data=planets, x='year')

: Creates a count plot with year on the x-axis and count on the y-axis.
    - 

plt.title('Number of Planets Discovered per Year')

: Sets the title of the count plot.
    - 

plt.xlabel('Year')

: Sets the x-axis label.
    - 

plt.ylabel('Count')

: Sets the y-axis label.
    - 

plt.xticks(rotation=90)

: Rotates the x-axis labels by 90 degrees.
    - 

plt.show()

: Displays the plot.

- **Violin Plot**:
    - 

sns.catplot(x='method', y='orbital_period', data=planets, kind='bar', height=6, aspect=2)

: Creates a bar plot with detection method on the x-axis and orbital period on the y-axis.
    - 

plt.title('Average Orbital Period by Detection Method')

: Sets the title of the violin plot.
    - 

plt.xlabel('Detection Method')

: Sets the x-axis label.
    - 

plt.ylabel('Average Orbital Period (days)')

: Sets the y-axis label.
    - 

plt.show()

: Displays the plot.

## Limitations
- The project assumes that the datasets are clean and do not require preprocessing.
- The visualizations are limited to the capabilities of the Seaborn library.
- The project does not include advanced statistical analysis or machine learning techniques.

## Conclusion
This project provides a comprehensive guide to creating various types of plots using the Seaborn library in Python. By following the examples provided, users can effectively visualize and analyze their datasets to gain meaningful insights.
