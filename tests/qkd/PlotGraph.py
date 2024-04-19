import matplotlib.pyplot as plt
import json

# Load the data from the uploaded file
file_path = 'result.txt'

# Initialize lists to store the extracted data
distances = []
average_sifting_percentages = []
average_key_rates = []

# Open and read the entire file as a single JSON object
with open(file_path, 'r') as file:
    data = json.load(file)  # Use json.load() to read the whole file
    for key_rate in data:
        for distance in data[key_rate]:
            distances.append(int(distance))
            average_sifting_percentages.append(data[key_rate][distance]['average_sifting_percentage'])
            average_key_rates.append(data[key_rate][distance]['average_key_rate'])

# Plotting the graphs
# Plot for sifting percentage over distance
plt.figure(figsize=(10, 5))
plt.plot(distances, average_sifting_percentages, marker='o', linestyle='-', label='Average Sifting Percentage')
plt.title('Average Sifting Percentage over Distance')
plt.xlabel('Distance')
plt.ylabel('Average Sifting Percentage')
plt.grid(True)
plt.legend()
plt.savefig('sifting_percentage_over_distance.png')
plt.show()

# Plot for key rate over distance
plt.figure(figsize=(10, 5))
plt.plot(distances, average_key_rates, marker='o', linestyle='-', color='green', label='Average Key Rate')
plt.title('Average Key Rate over Distance')
plt.xlabel('Distance')
plt.ylabel('Average Key Rate')
plt.grid(True)
plt.legend()
plt.savefig('key_rate_over_distance.png')
plt.show()
