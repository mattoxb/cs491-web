#!/usr/bin/env python3

from datetime import datetime
import yaml

with open('dates','r') as file:
    dates = [line.strip() for line in file.readlines()]

with open('data/lectures.yml') as file:
    lectures = yaml.safe_load(file)

with open('data/lectures.yml', 'w') as f:
    for index, (key, content) in enumerate(lectures.items()):
        if 'date' in content and index < len(dates):
            content['date'] = dates[index]
        yaml.dump({key:content},f)

# # Sort the lectures by date
# lectures = dict(sorted(lectures.items(), key=lambda x: datetime.strptime(x[1]['date'], '%Y-%m-%d')))
# 
# # Save the modified YAML data back to the 'lectures.yaml' file
# with open('data/lectures.yml', 'w') as f:
#     yaml.dump(lectures, f)

print("Dates updated successfully.")

