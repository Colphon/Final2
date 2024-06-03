import csv
import re

def stats():
    filepath = 'stats.csv'
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        # Convert the list of lists into a single string with newline characters between rows
        data_string = "\n".join([": ".join(row) for row in data])
        # Update the label with the new string
        return data_string
def write(name, time):
    name_eligible = re.search('^[a-zA-Z0-9]{1,20}$', name.strip())
    if name_eligible:
        name = name.strip()
        with open('stats.csv', 'r', newline='') as review:
            reader = csv.reader(review)
            for row in reader:
                print(row[0])
                if name == row[0]:# Compare name with the first column
                    raise NameError
        with open('stats.csv', 'a', newline='') as stuffout:
            contentout = csv.writer(stuffout)
            contentout.writerow([name, time])

    else:
        raise ValueError

def determine_feed(feed):
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
def determine_pet(pet):
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
def determine_walk(walk):
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
def increase_feed(feed_value):
    if feed_value + 19 <= 100:
        feed_value += 20
    else:
        feed_value = 101
    return feed_value
def increase_pet(pet_value):
    if pet_value + 6 <= 100:
        pet_value += 7
    else:
        pet_value = 101
    return pet_value
def increase_walk(walk_value):
    if walk_value + 26 <= 100:
        walk_value += 27
    else:
        walk_value = 101
    return walk_value

