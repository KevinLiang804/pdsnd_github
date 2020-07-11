import time
import pandas as pd
import numpy as np
"Dictionary with csv and city"
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    cities = ["chicago", "new york city", "washington"]
    while city not in cities:
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city not in cities:
            print('Input not valid')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        month = input("Please select a month (january, february, march, april, may, june, or all): ").lower()
        if month not in months:
            print('Input not valid')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        day = input("Please select a day (monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all): ").lower()
        if day not in days:
            print('Input not valid')

    print('-'*70)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month: ',popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day: ',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station: ',popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station: ',popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combos'] = df['Start Station'] + " to " + df['End Station']
    popular_station_combo = df['Station Combos'].mode()[0]
    print('Most popular station combo: ', popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_duration = df['Trip Duration'].sum()
    print('Total travel time: ', sum_duration)

    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print('Average travel time: ', avg_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types: \n',user_types)

    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()
    print('Genders: \n',genders)


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    recent = df['Birth Year'].max()
    most_common = df['Birth Year'].mode()[0]

    print('Earliest birth year: ', earliest)
    print('Most recent birth year: ', recent)
    print('Most common birth year: ', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

def check_raw_data(df):
    "Prompts user to view more data. Each input will display 5 additional lines. This will continue until user hits no "
    total_rows = df.count
    check_raw = input("\nWould you like to see raw data? yes or no: ").lower()
    if check_raw == 'yes':
        a = 0
        b = 5
        while check_raw == 'yes':
            print(df.iloc[a:b])
            check_raw = input("\nWould you like to see more raw data? yes or no: ").lower()
            a += 5
            b += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        check_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
