import csv
import json


# Function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path):
  csv_data = []
  json_data = []

  # Read the CSV file
  with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      csv_data.append(row)

  # Convert CSV to JSON
  for row in csv_data:
    slide = {}
    if row['Slide number'] == '1':
      slide["type"] = "overview"

    if row['Location: Lat'] and row['Location: Lon']:
      slide["location"] = {
        "lat": float(row['Location: Lat']),
        "lon": float(row['Location: Lon'])
      }

    if row['Slide Title'] or row['Text. Note: You CAN use HTML tags here (50-60 words)']:
      slide["text"] = {
        "headline": row['Slide Title'],
        "text": row['Text. Note: You CAN use HTML tags here (50-60 words)']
      }

    if row['Media: URL']:
      slide["media"] = {
        "url": row['Media: URL'],
        "caption": row['Media: Caption'],
        "credit": row['Media: Credit']
      }

    json_data.append(slide)

  # Write to JSON file
  with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


# Call the function
csv_to_json("Story Map Slides - Slides-3.csv", "output.json")
