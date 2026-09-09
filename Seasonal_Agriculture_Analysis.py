import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load Farm Records
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Seasonal Yield & Profit Dynamics
season = (
    df.groupby('Season')[['Yield_Tonnes_Ha', 'Profit_INR']]
    .mean()
    .reindex(['Kharif', 'Rabi', 'Zaid'])
)
print('--- Seasonal Performance ---')
print(season)

# Irrigation Efficiency Benchmark
irr = (
    df.groupby('Irrigation_Method')[
        ['Water_Efficiency_t_per_1000m3', 'Profit_INR']
    ]
    .mean()
    .reindex(['Drip', 'Sprinkler', 'Rainfed', 'Flood'])
)
print('\n--- Irrigation Efficiency ---')
print(irr)
