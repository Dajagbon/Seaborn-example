import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/danie/Downloads/Exercise_Data.csv")

# Pivot the data for heatmap
pulse_data = data.melt(id_vars=['id', 'diet', 'kind'], value_vars=['1 min', '15 min', '30 min'], var_name='Time', value_name='Pulse')

# Create the heatmap
plt.figure(figsize=(10, 5))
heatmap_data = pulse_data.pivot_table(index='kind', columns='Time', values='Pulse')
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
plt.title('Heatmap of Pulse Data by Exercise Type and Time')
plt.xlabel('Time')
plt.ylabel('Exercise Type')
plt.show()

# Create a categorical plot
sns.catplot(x='diet', y='Pulse', hue='kind', kind='bar', data=pulse_data, height=5, aspect=2)
plt.title('Pulse Values by Diet Type and Exercise Type', fontsize=8, pad=3)
plt.xlabel('Diet Type')
plt.ylabel('Pulse')
plt.legend(title='Exercise Type')
plt.show()


# Load the planets dataset 
planets = sns.load_dataset('planets')

# Relational plots with Seaborn
# Create a scatter plot - Showing the relationship between distance and orbital_period
plt.figure(figsize=(10, 5))
sns.scatterplot(data=planets, x='distance', y='orbital_period', hue='method')
plt.title('Relationship between Distance and Orbital Period')
plt.xlabel('Distance (AU)')
plt.ylabel('Orbital Period (days)')
plt.legend(title='Detection Method')
plt.show()

# Create a line plot - Showing the relationship between year and mass for planets discovered  
plt.figure(figsize=(8, 6))
sns.lineplot(data=planets, x='year', y='mass', hue='method', marker='o')
plt.title('Yearly Discovery of Planet Mass')
plt.xlabel('Year')
plt.ylabel('Planet Mass (Jupiter Masses)')
plt.legend(title='Detection Method')
plt.show()

# Distributional plots with Seaborn
# Create a histogram - Showing the distribution of orbital_period
import seaborn as sns
import matplotlib.pyplot as plt

# Load the planets dataset
planets = sns.load_dataset('planets')

# Create the histogram
plt.figure(figsize=(10, 5))
sns.histplot(data=planets, x='orbital_period', kde=True)
plt.title('Distribution of Orbital Period')
plt.xlabel('Orbital Period (days)')
plt.ylabel('Frequency')

# Rotate the x-axis labels
plt.xticks(rotation=45)  # You can adjust the angle to suit your needs
plt.show()


# Create a box plot - Showing the distribution of mass by method
plt.figure(figsize=(8, 5))
sns.boxplot(data=planets, x='method', y='mass')
plt.title('Distribution of Planet Mass by Detection Method')
plt.xlabel('Detection Method')
plt.ylabel('Planet Mass (Jupiter Masses)')
plt.xticks(rotation=70)
plt.show()

# Categorical plots with Seaborn
# Create a bar plot - Showing the number of planets discovered each year
plt.figure(figsize=(10, 6))
sns.countplot(data=planets, x='year')
plt.title('Number of Planets Discovered per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Create a violin plot - Showing the average orbital_period for each method
sns.catplot(x='method', y='orbital_period', data=planets, kind='bar', height=6, aspect=2) 
plt.title('Average Orbital Period by Detection Method') 
plt.xlabel('Detection Method') 
plt.ylabel('Average Orbital Period (days)') 
plt.xticks(rotation=90) 
plt.show()