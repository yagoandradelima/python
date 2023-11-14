import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('databases\car_price.csv')

figures, axes = plt.subplot(nrows=2, ncols=2, figsize=(10,4))

print(dataset)

axes[0][0] = plt.scatter(dataset['wheelbase'], dataset['carlenght'], s=25)

