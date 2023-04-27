import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df["BMI"] = df["weight"]/((df["height"]/100)**2)
df['overweight'] = df["BMI"].apply(lambda x: 1 if x>=25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
#overweight
df["overweight"] = df["BMI"].apply(lambda x: 1 if x>=25 else 0)
#cholesterol
df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x>1 else 0)
#gluc
df["gluc"] = df["gluc"].apply(lambda x: 1 if x>1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco","cholesterol","gluc","overweight","smoke"], value_name='category_value')
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat
    # Draw the catplot with 'sns.catplot()'
    # create a chart showing the value counts of the categorical features
    fig =sns.catplot(data=df_cat, x='variable', hue='category_value', col='cardio',       kind='count',hue_order=[0,1])
  
    # get the legend object
    legend = fig._legend
    # set the title of the legend
    legend.set_title('value')
    #save plot
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025))]
    df_heat = df_heat[(df_heat['height'] <= df_heat['height'].quantile(0.975))]
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025))]
    df_heat = df_heat[(df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = round(df_heat.corr(),1)

    # Set the lower triangle of the correlation matrix to NaN
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(round(df.corr(),1), annot=True, cmap="cividis", mask=mask, ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
