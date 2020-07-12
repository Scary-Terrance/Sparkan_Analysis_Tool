# List for parsed data
parsed_data = []

def parse_data(path):
    # Load the file
    file = open(path, 'r')
    header_done = False
    for line in file:
        # Look for the 1 after the header
        if line[0] == '1':
            header_done = True
        # Header finished, parse line
        if header_done:
            # List for the current rows data
            row = []
            # Split the data for the row into a list around tabs
            line_data = line.split('\t')
            # Ignore first 2 data points, store the rest in the row list
            for i in range(2, len(line_data)):
                row.append(float(line_data[i]))
            # Add the row to the parsed_data variable
            parsed_data.append(row)
    file.close()

# Get the maximum data value value in rows min_row to max_row at specified collumn
def max_in_range(min_row, max_row, col):
    maximum = 0
    for i in range(min_row, max_row):
        # Data is larger than defined maximum
        if parsed_data[i][col] > maximum:
            maximum = parsed_data[i][col]
    return maximum

parse_data("test_data.txt")
print(max_in_range(0, 19, 3))
