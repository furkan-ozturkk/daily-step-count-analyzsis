import json
from datetime import datetime
from collections import defaultdict

# JSON file path
json_file = "C:/Users/furka/Desktop/DSA/step_count_data.json"

try:
    with open(json_file, "r", encoding="utf-8") as f:
        step_data = json.load(f)
    
    # Dictionary to group step counts by day for 2024
    daily_steps = defaultdict(int)

    for entry in step_data:
        # Extract date and check if it belongs to 2024
        start_date = datetime.strptime(entry["startDate"], "%Y-%m-%d %H:%M:%S %z")
        if start_date.year == 2024:
            # Calculate daily total (format: YYYY-MM-DD)
            day = start_date.strftime("%Y-%m-%d")
            daily_steps[day] += int(entry["value"])

    # Display results
    print("Daily step counts for the year 2024:")
    for day, steps in sorted(daily_steps.items()):
        print(f"{day}: {steps} steps")
        
except FileNotFoundError:
    print(f"Error: '{json_file}' file not found.")
except json.JSONDecodeError:
    print("Error: JSON file is not properly formatted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
