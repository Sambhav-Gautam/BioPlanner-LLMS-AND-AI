# Data from the table
data = [
    {"JSON ID": 1007, "Steps Length": 18, "Total Protocol Length in Tokens": 1175, "Tokens per Step": 65.28, "Tokens per Original Description": 240, "Tokens per Generated Description": 60},
    {"JSON ID": 1073, "Steps Length": 4, "Total Protocol Length in Tokens": 227, "Tokens per Step": 56.75, "Tokens per Original Description": 109, "Tokens per Generated Description": 68},
    {"JSON ID": 10051, "Steps Length": 18, "Total Protocol Length in Tokens": 1135, "Tokens per Step": 63.06, "Tokens per Original Description": 235, "Tokens per Generated Description": 97},
    {"JSON ID": 10157, "Steps Length": 15, "Total Protocol Length in Tokens": 348, "Tokens per Step": 23.2, "Tokens per Original Description": 5, "Tokens per Generated Description": 58},
    {"JSON ID": 10176, "Steps Length": 7, "Total Protocol Length in Tokens": 639, "Tokens per Step": 91.29, "Tokens per Original Description": 115, "Tokens per Generated Description": 83},
    {"JSON ID": 10256, "Steps Length": 16, "Total Protocol Length in Tokens": 861, "Tokens per Step": 53.81, "Tokens per Original Description": 29, "Tokens per Generated Description": 58},
    {"JSON ID": 10279, "Steps Length": 6, "Total Protocol Length in Tokens": 238, "Tokens per Step": 39.67, "Tokens per Original Description": 15, "Tokens per Generated Description": 43},
    {"JSON ID": 10606, "Steps Length": 9, "Total Protocol Length in Tokens": 434, "Tokens per Step": 48.22, "Tokens per Original Description": 90, "Tokens per Generated Description": 58},
    {"JSON ID": 10614, "Steps Length": 13, "Total Protocol Length in Tokens": 677, "Tokens per Step": 52.08, "Tokens per Original Description": 33, "Tokens per Generated Description": 83},
    {"JSON ID": 10626, "Steps Length": 11, "Total Protocol Length in Tokens": 547, "Tokens per Step": 49.73, "Tokens per Original Description": 112, "Tokens per Generated Description": 76},
    {"JSON ID": 10238, "Steps Length": 23, "Total Protocol Length in Tokens": 697, "Tokens per Step": 30.3, "Tokens per Original Description": 213, "Tokens per Generated Description": 83},
    {"JSON ID": 10650, "Steps Length": 10, "Total Protocol Length in Tokens": 300, "Tokens per Step": 30.0, "Tokens per Original Description": 12, "Tokens per Generated Description": 46},
    {"JSON ID": 10703, "Steps Length": 12, "Total Protocol Length in Tokens": 658, "Tokens per Step": 54.83, "Tokens per Original Description": 36, "Tokens per Generated Description": 71},
    {"JSON ID": 10779, "Steps Length": 15, "Total Protocol Length in Tokens": 768, "Tokens per Step": 51.2, "Tokens per Original Description": 24, "Tokens per Generated Description": 58},
    {"JSON ID": 10832, "Steps Length": 12, "Total Protocol Length in Tokens": 1037, "Tokens per Step": 86.42, "Tokens per Original Description": 24, "Tokens per Generated Description": 64},
    {"JSON ID": 10880, "Steps Length": 15, "Total Protocol Length in Tokens": 605, "Tokens per Step": 40.33, "Tokens per Original Description": 81, "Tokens per Generated Description": 79},
    {"JSON ID": 10903, "Steps Length": 19, "Total Protocol Length in Tokens": 576, "Tokens per Step": 30.32, "Tokens per Original Description": 19, "Tokens per Generated Description": 65},
    {"JSON ID": 10904, "Steps Length": 4, "Total Protocol Length in Tokens": 92, "Tokens per Step": 23.0, "Tokens per Original Description": 8, "Tokens per Generated Description": 62},
    {"JSON ID": 10906, "Steps Length": 8, "Total Protocol Length in Tokens": 540, "Tokens per Step": 67.5, "Tokens per Original Description": 36, "Tokens per Generated Description": 53},
    {"JSON ID": 10907, "Steps Length": 4, "Total Protocol Length in Tokens": 87, "Tokens per Step": 21.75, "Tokens per Original Description": 15, "Tokens per Generated Description": 65},
    {"JSON ID": 10908, "Steps Length": 6, "Total Protocol Length in Tokens": 117, "Tokens per Step": 19.5, "Tokens per Original Description": 18, "Tokens per Generated Description": 69},
    {"JSON ID": 10909, "Steps Length": 9, "Total Protocol Length in Tokens": 187, "Tokens per Step": 20.78, "Tokens per Original Description": 16, "Tokens per Generated Description": 56},
    {"JSON ID": 10920, "Steps Length": 14, "Total Protocol Length in Tokens": 580, "Tokens per Step": 41.43, "Tokens per Original Description": 17, "Tokens per Generated Description": 55},
    {"JSON ID": 10921, "Steps Length": 16, "Total Protocol Length in Tokens": 917, "Tokens per Step": 57.31, "Tokens per Original Description": 100, "Tokens per Generated Description": 58},
    {"JSON ID": 10936, "Steps Length": 16, "Total Protocol Length in Tokens": 652, "Tokens per Step": 40.75, "Tokens per Original Description": 28, "Tokens per Generated Description": 52}
]

# Calculating statistics
num_protocols = len(data)
avg_steps = sum(protocol["Steps Length"] for protocol in data) / num_protocols
avg_total_length = sum(protocol["Total Protocol Length in Tokens"] for protocol in data) / num_protocols
avg_tokens_per_step = sum(protocol["Tokens per Step"] for protocol in data) / num_protocols
avg_tokens_per_original = sum(protocol["Tokens per Original Description"] for protocol in data) / num_protocols
avg_tokens_per_generated = sum(protocol["Tokens per Generated Description"] for protocol in data) / num_protocols

import matplotlib.pyplot as plt

# Data for the table
statistics = {
    "Protocols": num_protocols,
    "Average number of steps": avg_steps,
    "Average total protocol length in tokens": avg_total_length,
    "Average tokens per step": avg_tokens_per_step,
    "Average tokens per original description": avg_tokens_per_original,
    "Average tokens per generated description": avg_tokens_per_generated,
}

# Create a bar chart
fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(statistics.keys(), statistics.values(), color='blue')

# Adding the text labels for each bar
for key, value in statistics.items():
    ax.text(key, value + 0.5, f'{value:.2f}', ha='center')

# Setting labels and title
ax.set_ylabel('Value')
ax.set_title('Statistics Summary')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Save the plot as an image file
plt.savefig('statistics_summary.png')

# Show plot
plt.show()