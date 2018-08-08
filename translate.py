import boto3
import csv
import sys

# Using AWS Translate API to translate a CSV file

if len(sys.argv)!=2:
    print("Usage: python translate.py input.csv");
    sys.exit();
input = str(sys.argv[1])
output = input[:-4] + '-output.csv'
translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

print(output)
with open(input, newline='') as input:
    with open(output, 'w', newline='') as output:
        reader = csv.reader(input, delimiter=',', quotechar='"')
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            if row[1]!="":
                print(row[1])
                result = translate.translate_text(Text=row[1], SourceLanguageCode="de", TargetLanguageCode="en")
                writer.writerow([row[0],row[1],result.get('TranslatedText')])
            else:
                writer.writerow([row[0],row[1],""])
