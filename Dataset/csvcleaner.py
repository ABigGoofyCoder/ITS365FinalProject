import csv

def clean_password_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write header if it exists
        header = next(reader)
        if len(header) == 2 and header[0].lower() == 'password' and header[1].lower() == 'strength':
            writer.writerow(header)
        else:
            # If no proper header, reset to beginning
            infile.seek(0)
            reader = csv.reader(infile)

        for row in reader:
            if len(row) == 2:
                password, strength = row
                if ',' not in password:
                    writer.writerow([password, strength])

if __name__ == "__main__":
    input_csv = 'data.csv'          # Original CSV filename
    output_csv = 'cleaned_data.csv'  # New cleaned CSV filename
    clean_password_csv(input_csv, output_csv)
    print(f"Finished cleaning. Cleaned file saved as '{output_csv}'")
