import json
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

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

    # Sort data by date
    sorted_dates = sorted(daily_steps.keys())
    sorted_steps = [daily_steps[date] for date in sorted_dates]

    # Create a larger and clearer bar chart
    plt.figure(figsize=(14, 8))
    bars = plt.bar(sorted_dates, sorted_steps, color='skyblue', edgecolor='blue')

    # Add labels and title
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Steps", fontsize=14)
    plt.title("Daily Step Counts for 2024", fontsize=16, weight='bold')
    plt.xticks(rotation=45, fontsize=10)  # Rotate date labels
    plt.yticks(fontsize=10)
    
    # Add step count values on top of bars
    for bar, steps in zip(bars, sorted_steps):
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # X position
            bar.get_height() + 50,             # Y position
            f"{steps}",                        # Text to display
            ha='center', va='bottom', fontsize=10
        )

    # Adjust layout for better visibility
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

    # Show the plot
    plt.show()

except FileNotFoundError:
    print(f"Error: '{json_file}' file not found.")
except json.JSONDecodeError:
    print("Error: JSON file is not properly formatted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
