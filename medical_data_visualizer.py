import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df=pd.read_csv('medical_examination.csv')
df = None

# 2
overweight = df['weight']/((df['height']/100)**2)
overweight[overweight<25]=0
overweight[overweight>=25]=1
df['overweight'] = overweight
df['overweight'] = None

# 3
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].replace(1, 0)
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].replace([2,3], 1)
# 4
df_cardio_0=df[df['cardio']==0]
plt.hist([df_cardio_0.active, df_cardio_0.alco, df_cardio_0.smoke, df_cardio_0.gluc, df_cardio_0.cholesterol], bins=2)
plt.legend(['Active', 'Alcohol', 'Smoke', 'Gluc', 'Cholesterol'])
plt.title('Cardio = 0');

df_cardio_1=df[df['cardio']==1]
plt.hist([df_cardio_1.active, df_cardio_1.alco, df_cardio_1.smoke, df_cardio_1.gluc, df_cardio_1.cholesterol], bins=2)
plt.legend(['Active', 'Alcohol', 'Smoke', 'Gluc', 'Cholesterol'])
plt.title('Cardio = 0');
    
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
