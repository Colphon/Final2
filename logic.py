import csv
import re

def stats() -> str:
    '''
    Method that reads stats.csv and returns a string to be displayed in stat_window.
    '''
    filepath = 'stats.csv'
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        # Convert the list of lists into a single string with newline characters between rows
        data_string = "\n".join([": ".join(row) for row in data])
        # Update the label with the new string
        return data_string
def write(name: str, time: float) -> None:
    '''
    Method that checks the inputted name. The name must be alphanumeric and between 1 and 20 characters, or else a ValueError is raised.
    Afterward, the name is compared to the column of names in stats.csv and if it matches a name a NameError is raised.
    If no errors occur, the name and time are written to stats.csv.
    '''
    name_eligible = re.search('^[a-zA-Z0-9]{1,20}$', name.strip())
    if name_eligible:
        name = name.strip()
        with open('stats.csv', 'r', newline='') as review:
            reader = csv.reader(review)
            for row in reader:
                if row:
                    if name == row[0]:# Compare name with the first column
                        raise NameError
        with open('stats.csv', 'a', newline='') as stuffout:
            contentout = csv.writer(stuffout)
            contentout.writerow([name, time])

    else:
        raise ValueError

def determine_feed(feed: int) -> int:
    '''
    Method that determines the value of the feed modifier.
    '''
    if feed > 85:
        return 5
    elif feed > 40:
        return 2
    elif feed > 30:
        return -2
    elif feed > 20:
        return -4
    elif feed > 0:
        return -5
    else:
        return -10
def determine_pet(pet: int) -> int:
    '''
    Method that determines the value of the pet modifier.
    '''
    if pet > 75:
        return 3
    elif pet > 65:
        return 1
    elif pet > 50:
        return 0
    elif pet > 30:
        return -1
    elif pet > 20:
        return -2
    elif pet > 0:
        return -4
    else:
        return -10
def determine_walk(walk: int) -> int:
    '''
    Method that determines the value of the walk modifier.
    '''
    if walk > 80:
        return 5
    elif walk > 45:
        return 2
    elif walk > 25:
        return 1
    elif walk > 0:
        return -3
    else:
        return -10

# net gain is the value added to the progress value in the if statement of increase_progress - counter needed to execute if statement
def increase_feed(feed_value: int) -> int:
    '''
    Method that determines the value of the feed progressbar
    '''
    if feed_value + 19 <= 100:
        feed_value += 20
    else:
        feed_value = 101
    return feed_value
def increase_pet(pet_value: int) -> int:
    '''
    Method that determines the value of the pet progressbar
    '''
    if pet_value + 6 <= 100:
        pet_value += 7
    else:
        pet_value = 101
    return pet_value
def increase_walk(walk_value: int) -> int:
    '''
    Method that determines the value of the walk progressbar
    '''
    if walk_value + 26 <= 100:
        walk_value += 27
    else:
        walk_value = 101
    return walk_value

