import json

def end_of_round(distance, file_name='round_details.txt', output_file='result.txt'):
    total_sifting_percentage = 0
    total_key_rate = 0
    round_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            try:
                # Extracting the JSON string from the line
                json_str = line.split(':', 1)[1].strip()
                detail_dict = json.loads(json_str)
                total_sifting_percentage += detail_dict['sifting_percentage']
                total_key_rate += detail_dict['key_rate']
                round_count += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    if round_count > 0:
        average_sifting_percentage = total_sifting_percentage / round_count
        average_key_rate = total_key_rate / round_count
    else:
        average_sifting_percentage = 0
        average_key_rate = 0

    # Load the existing results and update or add the new entry
    try:
        with open(output_file, 'r') as file:
            existing_results = {int(entry['distance']): entry for entry in (json.loads(line) for line in file)}
    except FileNotFoundError:
        existing_results = {}

    # Update or add the current entry
    existing_results[distance] = {
        'distance': distance,
        'average_sifting_percentage': average_sifting_percentage,
        'average_key_rate': average_key_rate
    }

    # Write the updated results back to the file
    with open(output_file, 'w') as file:
        for entry in existing_results.values():
            json.dump(entry, file)
            file.write('\n')

    print(f"Average Sifting Percentage: {average_sifting_percentage}")
    print(f"Average Key Rate: {average_key_rate}")

if __name__ == "__main__":
    end_of_round(10)
