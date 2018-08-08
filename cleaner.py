import csv
import sys

# Delete row from CSV file if value if second cell is empty

if len(sys.argv)!=2:
    print("Usage: python cleaner.py input.csv");
    sys.exit();
input = str(sys.argv[1])
output = input[:-4] + '-output.csv'

print(output)
with open(input, newline='') as input:
    with open(output, 'w', newline='') as output:
        reader = csv.reader(input, delimiter=',', quotechar='"')
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            if row[1]!="":
                print(row[1])
                writer.writerow([row[0],row[1]])
