import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df["race"].value_counts()

  # What is the average age of men?
  man = df[df['sex'] == "Male"]
  average_age_men = round(man['age'].mean(), 1)

  # What is the percentage of people who have a Bachelor's degree?
  bachelor = df['education'].value_counts(
    normalize=True).apply(lambda x: x * 100)
  percentage_bachelors = round(bachelor['Bachelors'], 1)
  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  filter_list = ['Bachelors', 'Masters', 'Doctorate']

  # What percentage of people without advanced education make more than 50K?
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = len(df[df['education'].isin(filter_list)])
  lower_education = len(df[~df['education'].isin(filter_list)])

  higher_education_df = df[df['education'].isin(filter_list)]
  low_education_df = df[~df['education'].isin(filter_list)]

  salary = higher_education_df[higher_education_df['salary'] == '>50K']
  perc = (len(salary) / len(higher_education_df)) * 100

  salary_50 = low_education_df[low_education_df['salary'] == '>50K']
  perc_50 = (len(salary_50) / len(low_education_df)) * 100

  # percentage with salary >50K
  higher_education_rich = round(perc, 1)
  lower_education_rich = round(perc_50, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df["hours-per-week"].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K !!!!!!!!!!
  min_more50 = df[df["hours-per-week"] == df["hours-per-week"].min()]
  len(min_more50[min_more50['salary'] == ">50K"]) / len(min_more50) * 100
  rich_percentage = len(
    min_more50[min_more50['salary'] == ">50K"]) / len(min_more50) * 100

  # What country has the highest percentage of people that earn >50K?
  # calculate the total count of employees for each country
  grouped = df.groupby(['native-country',
                        'salary']).size().reset_index(name='Count')

  #Calculate the total count of employees for each country
  total_count = grouped.groupby(
    ['native-country'])['Count'].sum().reset_index(name='Total Count')

  #merge
  merged = pd.merge(grouped, total_count, on='native-country')

  # calculate country
  merged["Percentage"] = merged["Count"] / merged["Total Count"] * 100

  country = merged[merged["salary"] == ">50K"]
  country_max = country[country["Percentage"] == country["Percentage"].max()]
  highest_earning_country = country_max["native-country"].iloc[0]
  highest_earning_country_percentage = round(country_max["Percentage"].iloc[0],
                                             1)

  # Identify the most popular occupation for those who earn >50K in India.
  popular = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]
  popular = popular["occupation"].value_counts()
  country_max = popular.idxmax()
  top_IN_occupation = country_max

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
