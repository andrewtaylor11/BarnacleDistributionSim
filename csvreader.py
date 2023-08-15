import csv

# Read circle data from CSV file
circles = []
with open('circle_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        x, y, radius = map(float, row)
        diameter = 2 * radius
        circles.append(diameter)

# Calculate average circle diameter
if circles:
    average_diameter = sum(circles) / len(circles)
    num_circles = len(circles)
    print("Number of Circles:", num_circles)
    print("Average Circle Diameter:", average_diameter)
else:
    print("No circle data found.")
