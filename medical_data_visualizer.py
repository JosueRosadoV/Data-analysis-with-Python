import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
df = None

# 2
overweight=df['weight']/((df['height']/100)**2)
overweight[overweight<25]=0
overweight[overweight>=25]=1
df['overweight'] = overweight
df['overweight'] = None

# 3
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].replace(1, 0)
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].replace([2,3], 1)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'smoke', 'gluc', 'cholesterol', 'overweight'])
    df_cat = None


    # 6
    df_1=df_cat[df_cat.cardio==0]
sns.catplot(x='value',col="variable", col_wrap=4,
                data=df_1,
                kind="count");

df_2=df_cat[df_cat.cardio==1]
sns.catplot(x='value',col="variable", col_wrap=4,
                data=df_2,
                kind="count");
    df_cat = None
    

    # 7



    # 8
fig = plt.savefig('foo.png')
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = pd.read_csv('medical_examination.csv')
    overweight=df_heat['weight']/((df_heat['height']/100)**2)
    overweight[overweight<25]=0
    overweight[overweight>=25]=1
    df_heat['overweight'] = overweight

    df_heat = df_heat.drop(df_heat[df_heat['ap_lo']>df_heat['ap_hi']].index)
    df_heat = df_heat.drop(df_heat[(df_heat.height<df_heat.height.quantile(0.025)) | (df_heat.height>df_heat.height.quantile(0.975))].index)
    df_heat = df_heat.drop(df_heat[(df_heat.weight<df_heat.weight.quantile(0.025)) | (df_heat.weight>df_heat.weight.quantile(0.975))].index)
    df_heat = None

    # 12
    corr=df_heat.corr()
    corr = None

    # 13
    mask = True



    # 14
    fig, ax = None

    # 15
    sns.heatmap(corr, annot=True);


    # 16
    fig.savefig('heatmap.png')
    return fig
