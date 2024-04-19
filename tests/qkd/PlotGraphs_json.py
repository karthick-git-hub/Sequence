from itertools import cycle

import matplotlib.pyplot as plt
import json
import os


def plot_combined_graphs(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract the directory from the file_path
    directory = os.path.dirname(file_path)
    # Define markers and line styles
    markers = cycle(['o', 'x', '*'])  # Extend this list as needed
    line_styles = cycle(['-', '--', '-.'])  # Extend this list as needed

    for attenuation_level, measurements in data.items():
        # Sort the keys to ensure correct plotting order
        distances = sorted(measurements.keys(), key=int)
        sg_sifting_percentages = [measurements[distance]['average_sifting_percentage'] for distance in distances]

        # Plot sg_average_sifting_percentage for each attenuation level
        plt.plot(distances, sg_sifting_percentages, marker=next(markers), linestyle=next(line_styles), label=f'Attenuation: {attenuation_level}')

    # plt.title('Savitzky-Golay Filtered Sifting Percentage')
    plt.xlabel('Distance')
    plt.ylabel('Average Sifting Percentage (%)')
    # plt.grid(True)
    plt.ylim(0, 100)
    plt.legend()
    plt.savefig(os.path.join(directory, 'combined_sg_sifting_percentage.png'))
    plt.show()

    for attenuation_level, measurements in data.items():
        distances = sorted(measurements.keys(), key=int)
        sg_sifting_percentages = [measurements[distance]['average_sifting_percentage'] for distance in distances]
        # Perform the subtraction element-wise
        qber = [(100 - percentage) / 100 for percentage in sg_sifting_percentages]
        # Plot sg_average_sifting_percentage for each attenuation level
        plt.plot(distances, qber, marker=next(markers), linestyle=next(line_styles), label=f'Attenuation: {attenuation_level}')

    # plt.title('Savitzky-Golay Filtered Sifting Percentage')
    plt.xlabel('Distance')
    plt.ylabel('QBER (%)')
    # plt.grid(True)
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig(os.path.join(directory, 'combined_sg_qber_percentage.png'))
    plt.show()


    for attenuation_level, measurements in data.items():
        # Sort the keys to ensure correct plotting order
        distances = sorted(measurements.keys(), key=int)
        sg_key_rates = [measurements[distance]['average_key_rate'] for distance in distances]

        # Plot sg_average_key_rate for each attenuation level
        plt.plot(distances, sg_key_rates, marker=next(markers), linestyle=next(line_styles), label=f'Attenuation: {attenuation_level}')
   
    # plt.title('Savitzky-Golay Filtered Key Rate')
    plt.xlabel('Distance')
    plt.ylabel('Average Key Rate')
    # plt.grid(True)
    plt.ylim(0, 0.4)
    plt.legend()
    plt.savefig(os.path.join(directory, 'combined_sg_key_rate.png'))
    plt.show()


# Usage example
file_path = 'Results/COW/P2p/results.json'  # Adjust the path to your preprocessed JSON file
plot_combined_graphs(file_path)
