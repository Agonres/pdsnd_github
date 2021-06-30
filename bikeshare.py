#!/usr/bin/env python
# coding: utf-8

# In[15]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print(CITY_DATA)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    cities=['chicago','new york city','washington']
    months=['january','february','march', 'april','may','june']
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n You can have information of the next cities: chicago, new york city, washington. Please choose one option.\n")
        if city not in cities:
            print("Incorrect word, please write the name of city in lower letter.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n Please choose one month: january, february, march, april, may, june. \n")
        if month !='all' and month not in months:
            print("Incorrect word, please write the month in lower letter.")
            continue
        else:
            break    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Please choose one day: monday, tuesday, wednesday, thursday, friday, saturday, sunday. \n")
        if day !='all' and day not in days:
            print("Incorrect word, please write the day in lower letter.")
            continue
        else:
            break
            
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
    
#extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

#Creating 'hour' variable
    df['hour'] = df['Start Time'].dt.hour
    

# filter by month if applicable
    if month != 'all':
        months=['january','february','march', 'april','may','june']
        # use the index of the months list to get the corresponding int
        month = months.index(month)+1 

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
    print('Most Frequent month:', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day_of_week:', popular_day)
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #start_station = df['Start Station'].value_counts().idxmax(skipna = True)
    start_station =df['Start Station'].value_counts().sort_values(ascending=False).head(1)
    
    print('Most commonly used start station:\n',start_station)

    # TO DO: display most commonly used end station
    #end_station = df['End Station'].value_counts().idxmax(skipna = True)
    end_station = df['End Station'].value_counts().sort_values(ascending=False).head(1)
    
    print('Most commonly used end station:\n',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end=df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False).head(1)
    
    print('Most frequent combination of start station and end station trip: \n',start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df['Trip Duration'].sum()
    print('total travel time in hours:',travel_time/3600)
    
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time in minutes:',mean_travel_time/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('counts of gender:\n', count_gender)
    except KeyError:
        print("\ncounts of gender:\nSorry. There is not information to solve this query.")
    
    
#There is a problem with washington,march and wednesday data.Therefore, we have to use try and except clauses

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min()
        print('earliest Birth Year:\n',earliest)
    except KeyError:
        print("\nearliest Birth Year:\nSorry. There is not information to solve this query.")
    
    try:
        most_recent=df['Birth Year'].max()
        print('most recent Birth Year:\n',most_recent)
    except KeyError:
        print("\nmost recent Birth Year\nSorry. There is not information to solve this query.")

    try:
        most_common=df['Birth Year'].value_counts().sort_values(ascending=False).head(1)
        print('most common Birth Year:\n',most_common)
    except KeyError:
        print("\nmost common Birth Year\nSorry. There is not information to solve this query.")
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
    


# In[ ]:




