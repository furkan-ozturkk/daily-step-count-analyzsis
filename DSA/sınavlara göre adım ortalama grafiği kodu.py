import json
from datetime import datetime
import matplotlib.pyplot as plt

# JSON file path
json_file = "C:/Users/furka/Desktop/DSA/step_count_data.json"

# List of exam dates (YYYY-MM-DD format)
exam_dates = [
    "2024-11-02", "2024-11-03", "2024-11-10", "2024-11-12",
    "2024-11-16", "2024-12-01", "2024-12-07", "2024-12-14", "2024-12-24"
]

try:
    with open(json_file, "r", encoding="utf-8") as f:
        step_data = json.load(f)

    # Separate steps for exam days and non-exam days
    exam_day_steps = []
    non_exam_day_steps = []

    # Group steps by day
    daily_steps = {}
    for entry in step_data:
        # Extract date
        start_date = datetime.strptime(entry["startDate"], "%Y-%m-%d %H:%M:%S %z")
        day = start_date.strftime("%Y-%m-%d")

        # Accumulate daily steps
        if day not in daily_steps:
            daily_steps[day] = 0
        daily_steps[day] += int(entry["value"])

    # Categorize steps into exam and non-exam days
    for day, steps in daily_steps.items():
        if day in exam_dates:
            exam_day_steps.append(steps)
        else:
            non_exam_day_steps.append(steps)

    # Calculate averages
    exam_day_average = sum(exam_day_steps) / len(exam_day_steps) if exam_day_steps else 0
    non_exam_day_average = sum(non_exam_day_steps) / len(non_exam_day_steps) if non_exam_day_steps else 0

    # Data for the bar chart
    labels = ["Exam Days", "Non-Exam Days"]
    averages = [exam_day_average, non_exam_day_average]

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, averages, color=['purple', 'green'], edgecolor='black')

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
    plt.title("Comparison of Step Counts: Exam Days vs. Non-Exam Days (2024)", fontsize=16, weight='bold')

    # Show the plot
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: '{json_file}' file not found.")
except json.JSONDecodeError:
    print("Error: JSON file is not properly formatted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
