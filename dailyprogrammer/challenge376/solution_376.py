
# initial code - iterates over each year in range and applies logic

import time

year_start = 123456789101112
year_end = 1314151617181920
years = year_end - year_start


def main():
    start = time.time()
    leap_years = 0
    
    for year in range(years):
        if isleap(year_start + year):
            leap_years += 1

    end = time.time()
    runtime = round((end - start) * 1000, 2)
    print(leap_years)
    print(runtime, "ms")


def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 900 == 200 or year % 900 == 600:
                return True
        else:
            return True


if __name__ == "__main__":
    main()