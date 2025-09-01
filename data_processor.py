import csv

def save_to_csv(data, filename):
    """
    Saves a list of dictionaries to a CSV file.
    """
    if not data:
        print("No data to save.")
        return
        
    print(f"Saving data to {filename}...")
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['quote', 'author', 'tags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            # Join the list of tags into a single string for the CSV
            row['tags'] = ', '.join(row['tags'])
            writer.writerow(row)
    print("Data saved successfully.")