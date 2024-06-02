import csv

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
    with open('stats.csv', 'a', newline='') as stuffout:
        contentout = csv.writer(stuffout)
        contentout.writerow([name, time])

