def main():
    time = input("What time is it?: ")
    x = convert(time)
    if 7.0 <= x <= 8.0:
        print('Breakfast')
    elif 12.0 <= x <= 13.0:
        print('Lunch')
    elif 18.0 <= x <= 19.0:
        print('Dinner')


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
