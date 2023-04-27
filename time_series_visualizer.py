import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col='date', parse_dates=True)

# Clean data
# Calculate the cutoff values for the top and bottom 2.5%
cutoff_low = df["value"].quantile(0.025)
cutoff_high = df["value"].quantile(0.975)
df = df[(df["value"]>=cutoff_low)&(df["value"]<=cutoff_high)]


def draw_line_plot():
    # Draw line plot
    #create a line plot using plt.plot()
    fig, ax = plt.subplots(figsize = (15,5))
    ax.plot(df.index, df['value'], color = 'r')
    # Set the xticks to every 6 months
    start_date = df.index[0].strftime('%Y-%m')
    end_date = df.index[-1].strftime('%Y-%m')
    xticks = pd.date_range(start=start_date, end=end_date, freq='6M')
    ax.set_xticks(xticks)
    #label
    ax.set_title("Daily freeCodeCamp Forum Page Views 05/2016 - 12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_grouped = df_bar
    # Draw bar plot
    df_grouped.index.names = ['Year', 'Month']
    # Group the data by year and month and calculate the mean page views for each group
    df_pivot = df_grouped.pivot_table(values='value', index= 'Year', columns='Month')
    # Define the month labels and colors for the plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    colors = ['#3CB371', '#FFA07A', '#FFD700', '#808080', '#9370DB', '#6495ED', '#7FFF00', '#F08080', '#00FFFF', '#FF69B4', '#C71585', '#0000CD']
    # Calculate the width of each bar
    width = 0.8 / len(months)
    # Create the bar chart using plt.bar()
    fig, ax = plt.subplots(figsize=(10, 7))
    # Add the month bars to the plot
    for i, month in enumerate(months):
        ax.bar(df_pivot.index + (i - len(months)/2) * width, df_pivot[i+1], width=width, color=colors[i])
    # Set xticks to integer year
    years = df_pivot.index.astype(int)
    ax.set_xticks(years)
    ax.set_xticklabels(years)
    # Customize the plot with the appropriate title, x-axis label, and y-axis label
    ax.set_title('Average Daily Page Views, by Month and Year')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(months, title='Months', loc='upper left')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # Create the figure and subplots
    fig, axs = plt.subplots(ncols=2, figsize=(12, 6))
    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=axs[0])
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Page Views")
    # Month-wise box plot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x="month", y="value", data=df_box, 
                order=month_order, ax=axs[1])
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_xlabel("Month")
    axs[1].set_ylabel("")
    # Adjust the layout and display the plot
    fig.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
