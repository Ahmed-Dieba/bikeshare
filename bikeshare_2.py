import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    c_in = False
    while c_in == False:
        city=input("Which city do you want to know about? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            c_in = True
        else:
            c_in = False
            print("Please choose a valid choice")
    
    # get user input for month (all, january, february, ... , june)
    m_in = False
    months=["january", "february", "march", "april", "may", "june","all"]
    while m_in == False:
        month=input("Which month do you want to filter by?\n (january, february, march, april, may, june)\n (type all if you don't want to filter): ").lower()
        if month in months:
            m_in = True
        else:
            m_in = False
            print("Please choose a valid choice")
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    d_in = False
    days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']
    while d_in == False:
        day=input("Choose a day Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n Type all if you want all days: ").lower()
        if day in days:
            d_in = True
        else:
            d_in = False
            print("Please choose a valid choice")


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
    df = pd.read_csv(CITY_DATA[city])
    #extract day and month from the information
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df["Start Time"].dt.month
    df['Day'] = df["Start Time"].dt.day_name()
    #filter by month
    if month != "all":
        months=["january", "february", "march", "april", "may", "june","all"]
        month = months.index(month) + 1
        df= df[df['Month'] == month]
    #filter by day
    if day !="all":
        df= df[df["Day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Here is the most common month --> ",df["Month"].mode()[0])


    # display the most common day of week
    print("Here is the most common day of week --> ",df["Day"].mode()[0])


    # display the most common start hour
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Hour"] = df["Start Time"].dt.hour
    print("Here is the most common hour --> ",df["Hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Here is the most commonly used start statiion --> ",df["Start Station"].mode()[0])


    # display most commonly used end station
    print("Here is the most commonly used end statiion --> ",df["End Station"].mode()[0])


    # display most frequent combination of start station and end station trip
    companation =df["Start Station"] +" --> "+ df["End Station"]
    print("Here is the most commonly used combination --> ",companation.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Here is the total travel time --> ", df["Trip Duration"].sum())


    # display mean travel time
    print("Here is the mean travel time --> ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Here is the number of user types -->",df['User Type'].value_counts())

    # Display counts of gender
    if city == "washington":
        print("Sorry, we don't have gender information for washington")
    else:
        print("Here is the gender information for the city -->",df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if city == "washington":
        print("Sorry, we don't have year of birth information for washington")
    else:
        print("Here is the most earliest year of birth -->",df['Birth Year'].min())
        print("Here is the most recent year of birth -->",df['Birth Year'].max())
        print("Here is the most common year of birth -->",df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def five_more(df):
    start = 0
    end = 5
    while True:
        response = input("Do you want to see some orginal data? (yes or no)").lower()
        if response == 'no':
            break
        elif response == 'yes':
            five_rows = df[start:end]
            print(five_rows)
            start+=5
            end+=5
        else:
            print("Please answer with yes of no")




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        five_more(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
