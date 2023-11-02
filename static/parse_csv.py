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
        "lon": float(row['Location: Lon']),
        "line": bool(row['Line']),
        "use_custom_marker": True,
        "icon": f"img/map_icon/{row['Icon']}"
      }

    if row['Slide Title'] or row['Text. Note: You CAN use HTML tags here (50-60 words)']:
      slide["text"] = {
        "headline": f"<span style=\"color: #2c2c2c; text-shadow: none;\">{row['Slide Title']} </span>",
        "text": f"<span style=\"color: #2c2c2c; text-shadow: none;\">{row['Text. Note: You CAN use HTML tags here (50-60 words)']} </span>"
      }

    if row['Media: URL']:
      slide["media"] = {
        "url": row['Media: URL'],
        "caption": f"<span style=\"color: #8e8e8e; text-shadow: none;\"> {row['Media: Caption']} </span>",
        "credit": f"<span style=\"color: #8e8e8e; text-shadow: none;\"> {row['Media: Credit']} </span>"
      }

    if row['Colour']:
      slide["background"] = {
        "color": row['Colour'],
        "opacity": int(row['Transparency'])
      }

    json_data.append(slide)

  storymap = {
    "width": 500,
    "height": 1800,
    "calculate_zoom": True,
    "storymap": {
      "language": "en",
      "map_type": "osm:standard",
      "map_as_image": False,
      "slides": json_data
    }
  }



  # Write to JSON file
  with open(json_file_path, 'w') as json_file:
    json.dump(storymap, json_file, indent=4)


# Call the function
csv_to_json("Story Map Slides - Slides-6.csv", "storymap.json")
