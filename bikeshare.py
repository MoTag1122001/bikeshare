import time
import pandas as pd
import numpnumpyy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ")
        city = city.lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print("invalid input,make sure to Choose from parentheses (chicago, new york city, washington)")
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input("Do you want filter the data to a particular month? If yes: type 'month name'  else: type 'all'").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("invalid input,make sure to Choose from within firist six months (all, january, february, ... , june) ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want to filter the data to a particular day? If yes: type 'day name' else type 'all'").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. make sure to Choose one from parentheses(all, monday, tuesday, ... sunday)  ")
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is : ", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("The most commonend station is : ", df['End Station'].mode()[0], "\n")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "/" + df['End Station']
    print("The most common trip from start to end is: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(),'sec'  , "\n")

    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean() ,'sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
    # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
    # Display earliest, most recent, and most common year of birth
        most_recent = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        earliest = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_common = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ",  earliest , "\n")
        print("The most recent year of birth is ", most_recent, "\n")
        print("The most common year of birth is ",  most_common , "\n")

        
def viwe_row (df):
    x = 1
    while True:
        raw = input('\nWould you like to see new 5 raws data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        viwe_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()