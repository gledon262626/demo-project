import pandas as pd
import numpy as np
import random

# Set a random seed for reproducibility
np.random.seed(42)

# Define flower characteristics
flower_types = ['Rose', 'Tulip', 'Daisy', 'Sunflower', 'Lily', 'Orchid']
colors = ['Red', 'Pink', 'Yellow', 'White', 'Purple', 'Orange']
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# Generate random data
num_samples = 100

data = {
    'flower_type': random.choices(flower_types, k=num_samples),
    'height_cm': np.random.uniform(10, 150, num_samples).round(1),
    'petal_length_cm': np.random.uniform(1, 10, num_samples).round(1),
    'petal_width_cm': np.random.uniform(0.5, 5, num_samples).round(1),
    'color': random.choices(colors, k=num_samples),
    'blooming_season': random.choices(seasons, k=num_samples),
    'price_usd': np.random.uniform(2, 50, num_samples).round(2),
    'lifespan_days': np.random.randint(3, 15, num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("\nFirst few rows of the dataset:")
print(df.head())

# Display some basic statistics
print("\nBasic statistics:")
print(df.describe())

# Display value counts for categorical columns
print("\nFlower type distribution:")
print(df['flower_type'].value_counts())

print("\nColor distribution:")
print(df['color'].value_counts())


