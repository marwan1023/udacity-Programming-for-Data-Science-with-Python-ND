import time
import pandas as pd
import numpy as np
import calendar
import matplotlib.pyplot as plt
import statistics  

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.
    In this project, you will make use of Python to explore dataEnter yes related to bike share systems for three major cities 
    in the United States—Chicago, New York City, and Washington. You will write code to import 
    the data and answer interesting questions about it by computing descriptive statistics. 
    You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
    """

    print(" WELCOME NANODEGREE PROGRAM FROM UDACITY:{Programming for Data Science with Python}")
    print("Marwan Saeed Alsharabbi")
    Returns=[" Asks user to specify a city, month, and day to analyze."
        "\n(str) city - name of the city to analyze"
        "\n(str) month - name of the month to filter by, or 'all' to apply no month filter"
        "\n(str) day - name of the day of week to filter by, or 'all' to apply no day filter"]
    print((" ").join(Returns))
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York city, or Washington?\n').lower()
    while city not in(CITY_DATA.keys()):
        print("You provided invalid city name Please insert the city name is correct.Please try again!")
        city = input('Would you like to see data for Chicago, New York city, or Washington?\n').lower()
    print('\nHello! Let\'s explore some US bikeshare data! {}'.format(city))
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month's data are you interested in? [January,February,March,April,May,June,All]. Please enter only in lower case!\n").lower()
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print("You provided invalid month name Please insert the month name is correct. Please try again!")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day's data are you interested in? (Monday-Tuesday-Wednesday-Thursday-Friday-Saturday-Sunday-All). Please enter only in lower case!\n").lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            break
        else:
            print("You provided invalid day name Please insert the day name is correct. Please try again!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    # Casting "Start Time" to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Get the weekday out of the "Start Time" value.
    df["month"] = df['Start Time'].dt.month  
    # Month-part from "Start Time" value.
    df["day_of_week"] = df['Start Time'].dt.weekday_name 
    # Hour-part from "Start Time" value.
    df["start_hour"] = df['Start Time'].dt.hour              
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    input_user()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')

    # display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    input_user()
   
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Popular start station: ",popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Popular end station: ",popular_end_station)

    # display most frequent combination of start station and end station trip
    trip_series = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_popular_trip = trip_series.describe()["top"]
    print('Most Popular trip is from ',most_popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    input_user()
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Convert seconds to readable time format
    def secs_to_readable_time(seconds):
        day = seconds // (24 * 3600)
        time = seconds % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        print('Days: {}, Hours: {}, Mins: {}, Secs: {}'.format(day,hour,minutes,seconds))

    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:\n')
    secs_to_readable_time(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {} seconds'.format(mean_travel_time))

    # TO DO: display min travel time
    min_trip =  df['Trip Duration'].min()
    print('\nmin Trip Duration: {} seconds'.format(min_trip))

    # TO DO: display max travel time
    max_trip =  df['Trip Duration'].max()
    print('\nmax Trip Duration: {} seconds'.format(max_trip))

    # TO DO: display medain travel time
    median_trip = df['Trip Duration'].median()
    print('\nmedain Trip Duration: {} seconds'.format(median_trip))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    input_user()
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
     #Display counts of user types
    print('Breakdown of users: ')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    print('\nBreakdown of gender: ')
    if 'Gender' in str(df.columns.values):
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Sorry! No gender data available for selected query.')
    # Display earliest, most recent, and most common year of birth
    print('\nBreakdown of birth year: ')
    if 'Birth Year' in str(df.columns.values):
        print('Earliest birth year is: ',df['Birth Year'].min())
        print('Latest birth year is: ',df['Birth Year'].max())
        print('Most common birth year is: ',df['Birth Year'].mode()[0])
    else:
        print('Sorry! No birth year data available for selected query.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    
    raw = input('\nWould you like to diplay raw data?please Enter yes\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break
def plot_stat(df):
    # If it's everything running as expected, check this graph!
    # Display counts of gender
    input_user()
    try:
        # if there is gender column get its count
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        # if there is no gender column like in washintgon print no data
        print("\nSorry! No Gender data available for selected query.!")
    try:
        #if there is birth year column get the most common value of it
        bmode = int(df['Birth Year'].value_counts().idxmax())
        print('Most common year of birth:', bmode)
    except KeyError:
        # if data is not found print no data
        print("\nSorry! No year of birth data available for selected query.!")
    print('Thank you!')    
    input('\nWould you like to exit? Enter yes to exit and any other key to continue.\n')
    # Display counts of Gender
    print('\nBreakdown of Gender: ')
    print("\nPlot a similar graph for Gender. Make sure the legend is correct")
    try:
        #Plot a similar graph for Gender. Make sure the legend is correct
        gender = df['Gender'].value_counts()
        types = ["Male", "Female"]
        quantity = gender
        y_pos = list(range(len(types)))
        plt.bar(y_pos, quantity)
        plt.ylabel('Quantity')
        plt.xlabel('Gender')
        plt.xticks(y_pos, types)
        plt.title('Quantity by Gender')
        plt.show(block=True)    
        print(gender)
    except KeyError:
        print("Sorry! No Gender data available for selected query.!")
        print('Thank you!')
        
    # Plot a similar graph for user_types. Make sure the legend is correct.
    print('\nPlot a similar graph for user_types. Make sure the legend is correct.')
    user_type = df['User Type'].value_counts()
    user_types = ["Customer", "Subscriber"]
    quantity = user_type
    y_pos = list(range(len(user_types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantity')
    plt.xlabel('User Type')
    plt.xticks(y_pos, user_types)
    plt.title('Quantity by User Type')
    plt.show(block=True)
    print(user_type)
def input_user():
    while True :
        exit = str(input('\nWould you like Displays statistics on bikeshare dataset ? Enter any  key to continue.\n '))
        if exit.lower()=='yes':
            break
        else:
            print('\nYou are being redirected to the start of the application.')
        return 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        plot_stat(df)
        exit = input('\nWould you like to exit? Enter yes to exit and any other key to continue.\n')
        if exit.lower()=='yes':
            print('Thank you!')
            break
        else:
            print('\nYou are being redirected to the start of the application.')
            print('-'*40)       
if __name__ == "__main__":
    main()
    
