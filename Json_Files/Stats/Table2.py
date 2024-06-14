import pandas as pd
import matplotlib.pyplot as plt
import json

# Data provided
data = [
    {
        "id": "1007",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 16,
        "number_lines_code_generated": 59
    },
    {
        "id": "1073",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 5,
        "number_lines_code_generated": 14
    },
    {
        "id": "10051",
        "number_pseudofunctions_edited": 1,
        "number_lines_code_edited": 7,
        "number_pseudofunctions_generated": 7,
        "number_lines_code_generated": 20
    },
    {
        "id": "10157",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 12,
        "number_lines_code_generated": 38
    },
    {
        "id": "10176",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 7,
        "number_lines_code_generated": 21
    },
    {
        "id": "10238",
        "number_pseudofunctions_edited": 2,
        "number_lines_code_edited": 21,
        "number_pseudofunctions_generated": 7,
        "number_lines_code_generated": 22
    },
    {
        "id": "10256",
        "number_pseudofunctions_edited": 1,
        "number_lines_code_edited": 10,
        "number_pseudofunctions_generated": 13,
        "number_lines_code_generated": 40
    },
    {
        "id": "10279",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 7,
        "number_lines_code_generated": 16
    },
    {
        "id": "10606",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 5,
        "number_lines_code_generated": 13
    },
    {
        "id": "10614",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 13,
        "number_lines_code_generated": 38
    },
    {
        "id": "10626",
        "number_pseudofunctions_edited": 2,
        "number_lines_code_edited": 13,
        "number_pseudofunctions_generated": 10,
        "number_lines_code_generated": 33
    },
    {
        "id": "10650",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 10,
        "number_lines_code_generated": 27
    },
    {
        "id": "10703",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 12,
        "number_lines_code_generated": 34
    },
    {
        "id": "10779",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 13,
        "number_lines_code_generated": 39
    },
    {
        "id": "10832",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 29,
        "number_lines_code_generated": 103
    },
    {
        "id": "10880",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 57,
        "number_lines_code_generated": 168
    },
    {
        "id": "10903",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 57,
        "number_lines_code_generated": 168
    },
    {
        "id": "10904",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 15,
        "number_lines_code_generated": 49
    },
    {
        "id": "10906",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 25,
        "number_lines_code_generated": 80
    },
    {
        "id": "10907",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 11,
        "number_lines_code_generated": 37
    },
    {
        "id": "10908",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 11,
        "number_lines_code_generated": 37
    },
    {
        "id": "10920",
        "number_pseudofunctions_edited": 6,
        "number_lines_code_edited": 51,
        "number_pseudofunctions_generated": 253,
        "number_lines_code_generated": 718
    },
    {
        "id": "10921",
        "number_pseudofunctions_edited": 7,
        "number_lines_code_edited": 72,
        "number_pseudofunctions_generated": 21,
        "number_lines_code_generated": 61
    },
    {
        "id": "10936",
        "number_pseudofunctions_edited": 0,
        "number_lines_code_edited": 0,
        "number_pseudofunctions_generated": 16,
        "number_lines_code_generated": 38
    }
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Calculate averages
average_pseudofunctions_edited = df['number_pseudofunctions_edited'].mean()
average_lines_code_edited = df['number_lines_code_edited'].mean()
average_pseudofunctions_generated = df['number_pseudofunctions_generated'].mean()
average_lines_code_generated = df['number_lines_code_generated'].mean()

# Calculate average pseudofunctions per protocol
average_pseudofunctions_per_protocol = df['number_pseudofunctions_generated'].mean()

# Calculate average pseudofunctions per step
total_pseudofunctions_generated = df['number_pseudofunctions_generated'].sum()
total_steps = df['number_lines_code_generated'].count()
average_pseudofunctions_per_step = total_pseudofunctions_generated / total_steps

# Calculate average lines of pseudocode
total_lines_code_generated = df['number_lines_code_generated'].sum()
average_lines_of_pseudocode = total_lines_code_generated / total_steps

# Print the averages
print(f"Average number of pseudofunctions edited: {average_pseudofunctions_edited:.2f}")
print(f"Average number of lines of code edited: {average_lines_code_edited:.2f}")
print(f"Average number of pseudofunctions generated: {average_pseudofunctions_generated:.2f}")
print(f"Average number of lines of code generated: {average_lines_code_generated:.2f}")
print(f"Average number of pseudofunctions per protocol: {average_pseudofunctions_per_protocol:.2f}")
print(f"Average number of pseudofunctions per step: {average_pseudofunctions_per_step:.2f}")
print(f"Average number of lines of pseudocode: {average_lines_of_pseudocode:.2f}")

# Create a table for the averages
averages_table = pd.DataFrame({
    "Category": ["Pseudofunctions Edited", "Lines of Code Edited", "Pseudofunctions Generated", "Lines of Code Generated",
                 "Pseudofunctions per Protocol", "Pseudofunctions per Step", "Lines of Pseudocode"],
    "Average Value": [
        average_pseudofunctions_edited,
        average_lines_code_edited,
        average_pseudofunctions_generated,
        average_lines_code_generated,
        average_pseudofunctions_per_protocol,
        average_pseudofunctions_per_step,
        average_lines_of_pseudocode
    ]
})

# Display the table
print("\nAverages Table:")
print(averages_table)

# Plotting the averages
plt.figure(figsize=(10, 6))
plt.barh(averages_table['Category'], averages_table['Average Value'], color='skyblue')
plt.xlabel('Average Value')
plt.title('Average Metrics for Pseudocode Editing and Generation')

# Adding the values on top of the bars
for index, value in enumerate(averages_table['Average Value']):
    plt.text(value + 0.2, index, f'{value:.2f}', va='center')

# Save the plot as an image
plt.tight_layout()
plt.savefig('average_metrics_plot.png')

# Show the plot
plt.show()
