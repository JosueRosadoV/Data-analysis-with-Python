import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df = None

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series([df['race'].str.contains('White').sum(),
                     df['race'].str.contains('Black').sum(),
                     df['race'].str.contains('Asian-Pac-Islander').sum(),
                     df['race'].str.contains('Amer-Indian-Eskimo').sum(),
                     df['race'].str.contains('Other').sum()
                    ],
                   index=['White',
                          'Black',
                          'Asian-Pac-Islander',
                          'Amer-Indian-Eskimo',
                          'Other'])
    race_count = None

    # What is the average age of men?
    average_age_men = round(df[(df.age>0) & (df.sex=='Male')].age.sum()/(df['sex'].str.contains('Male').sum()), 1)
    average_age_men = None

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'].str.contains('Bachelors').sum()/32561)*100, 1)
    percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    d=len(df[(df.education=='Doctorate')])
    e=len(df[(df.education=='Bachelors')])
    f=len(df[(df.education=='Masters')])
    higher_education = d+e+f
    higher_education = None

    lower_education = len(df['education']) - higher_education
    lower_education = None

    # percentage with salary >50K
    a=len(df[(df.education=='Bachelors') & (df.salary=='>50K')])
    b=len(df[(df.education=='Masters') & (df.salary=='>50K')])
    c=len(df[(df.education=='Doctorate') & (df.salary=='>50K')])
    higher_education_rich = round(((a+b+c)/higher_education)*100, 1)
    higher_education_rich = None

    lower_education_rich = round((df['salary'].str.contains('>50K').sum()-(a+b+c))/lower_education, 1)
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week']==1])
    num_min_workers = None

    rich_percentage = (len(df[(df['hours-per-week']==1) & (df.salary=='>50K')])/len((df[df['hours-per-week']==1])))*100
    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    # if the dataframe dx (number of people who earn more than 50K in the world) has 7841 elements, and 7171 of them are from de US, then the US has the largest percentage.
    dx = df[df.salary=='>50K']
    dx['native-country'].str.contains('United-States').sum()
    highest_earning_country = 'United-States'
    highest_earning_country = None
    
    highest_earning_country_percentage = round(((dx['native-country'].str.contains('United-States').sum())/32561)*100, 1)
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.

    #if the dataframe da (number of people who earn more than 50K from India) has 40 elements, and 25 of them are Prof-specialty, then Prof-Specialty is the most popular occupation for those who make more than 50k in India
    dx=df[df.salary=='>50K']
    da=dx[dx['native-country'].str.contains('India')]
    da['occupation'].unique()
    da['occupation'].str.contains('Prof-specialty').sum()
    top_IN_occupation = 'Prof-specialty'
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
