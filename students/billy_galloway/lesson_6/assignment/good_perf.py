"""
poorly performing, poorly written module

"""
import csv
import time
import datetime
import generate_data

def analyze(filename):
    '''
        ingests csv file and returns a tuple with
        a start time, end time, all the years found
        between 2013 and 2018
        and how many times that ao showed up in a row
    '''
    start = datetime.datetime.now()

    year_count = {
        '2013': 0,
        '2014': 0,
        '2015': 0,
        '2016': 0,
        '2017': 0,
        '2018': 0
    }

    found = 0

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lrow = list(row)
            date = f'{lrow[5]}'.split('/')
            year_count[date[-1]]+=1
            if 'ao' in row:
                found+=1

    end = datetime.datetime.now()

    return (start, end, year_count, found)

def main():
    ''' main method '''
    start = time.perf_counter()
    filename = "data/exercise-00.csv"
    # generate_data.write_csv(filename)
    output = analyze(filename)
    print(f'{output[2]}\nao was found {output[3]} times')
    end = time.perf_counter()
    total_time = end-start
    print(f'total time to finish {total_time}')

if __name__ == "__main__":
    main()
