import csv

sample_amount = 50
input_csv = 'INPUT_CSV_PATH'
output_csv = 'OUTPUT_CSV_PATH'

def extract_samples(input_csv, output_csv):
    try:
        with open(input_csv, 'r', newline='', encoding='utf-8') as infile, \
             open(output_csv, 'w', newline='', encoding='utf-8') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Read and write the header
            writer.writerow(next(reader))

            # Read and write the n entries
            for i, row in enumerate(reader):
                if i < sample_amount:
                    writer.writerow(row)
                else:
                    break

    except FileNotFoundError:
        print(f"The file {input_csv} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


extract_samples(input_csv, output_csv)
