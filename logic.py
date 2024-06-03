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
    name_eligible = re.match('^[a-zA-Z0-9]{1,20}$', name.strip())
    if name_eligible:
        name = name.strip()
        with open('stats.csv', 'r', newline='') as review:
            for line in review.readlines():
                match = re.match(name, line)
                if match:
                    raise NameError
        with open('stats.csv', 'a', newline='') as stuffout:
            contentout = csv.writer(stuffout)
            contentout.writerow([name, time])

    else:
        raise ValueError


