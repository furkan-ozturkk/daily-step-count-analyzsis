import json
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# JSON file path
json_file = "C:/Users/furka/Desktop/DSA/step_count_data.json"

try:
    with open(json_file, "r", encoding="utf-8") as f:
        step_data = json.load(f)

    # Group daily step totals for weekdays and weekends
    weekday_totals = defaultdict(int)
    weekend_totals = defaultdict(int)

    for entry in step_data:
        # Extract date
        start_date = datetime.strptime(entry["startDate"], "%Y-%m-%d %H:%M:%S %z")
        day = start_date.strftime("%Y-%m-%d")  # Group by day

        # Check if the date is a weekday (Monday=0 to Friday=4) or weekend (Saturday=5, Sunday=6)
        if start_date.weekday() < 5:
            weekday_totals[day] += int(entry["value"])
        else:
            weekend_totals[day] += int(entry["value"])

    # Calculate daily averages
    weekday_average = sum(weekday_totals.values()) / len(weekday_totals) if weekday_totals else 0
    weekend_average = sum(weekend_totals.values()) / len(weekend_totals) if weekend_totals else 0

    # Data for the bar chart
    labels = ["Weekdays", "Weekends"]
    averages = [weekday_average, weekend_average]

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, averages, color=['skyblue', 'salmon'], edgecolor='black')

    # Add average step counts inside bars
    for bar, avg in zip(bars, averages):
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # X position
            bar.get_height() / 2,              # Y position (center of the bar)
            f"{avg:.2f}",                      # Text to display
            ha='center', va='center', fontsize=12, color='white', weight='bold'
        )

    # Add labels and title
    plt.xlabel("Day Type", fontsize=14)
    plt.ylabel("Average Steps per Day", fontsize=14)
    plt.title("Comparison of Average Daily Step Counts: Weekdays vs. Weekends (2024)", fontsize=16, weight='bold')

    # Show the plot
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: '{json_file}' file not found.")
except json.JSONDecodeError:
    print("Error: JSON file is not properly formatted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
