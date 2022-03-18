# Read the file and store all lines in a list
file = open('report.txt', 'r')
lines = file.readlines()

# Go line by line from top till equal signs line and store all met lines in a list to remove the document header
lines_to_remove = []
for line in lines:
    if '====' not in line:
        lines_to_remove.append(line)
    else:
        break

for line in lines_to_remove:
    lines.remove(line)

# Remove the equal signs line
lines = [x for x in lines if "====" not in x]

# Cleanup and store all table headers in list
table_headers_string = lines[0].replace('\t', ' ')
table_headers_string = table_headers_string.replace('\n', ' ')
table_headers_string = ' '.join(table_headers_string.split())  # fixing multiple spaces to one space
table_headers = table_headers_string.split()
del table_headers[:2]  # Removing 'Def' and 'Size' from headers since first column is not needed

# Remove table headers from list
lines.pop(0)

# Cleanup all lines from multiple spaces, new line symbols and empty lines
cleaned_lines = []

for line in lines:
    new_line = line.replace('\n', '')
    new_line = ' '.join(new_line.split())
    if len(new_line) > 0:
        cleaned_lines.append(new_line)

# Store all lines as list of lists of strings divided by spaces
table_data = [x.split() for x in cleaned_lines]

# Remove the first column data since it is not needed
for row in table_data:
    row.pop(0)

# Find the minimum length of all rows and delete the last element of rows that exceed the minimum length. Just to get
# rid of random numbers in the end of some rows
minimum_row_length = min(map(len, table_data))
for row in table_data:
    if len(row) > minimum_row_length:
        del row[-1]

# Final calculations
for i in range(0, len(table_headers)):
    # Fetch all cells for every column and store them in list, excluding cells with dash symbol
    column_values = []
    for row in table_data:
        if '-' not in row[i]:
            column_values.append(row[i])
    # Deserialize all stored values to integers
    column_values_cleaned = []
    for value in column_values:
        cleaned_value = value.split('/')
        cleaned_value = map(int, cleaned_value)
        column_values_cleaned.extend(cleaned_value)

    # Sort the values for each column with bubble sorting since using builtin functions is not allowed.
    # Using column_values_cleaned.sort() would be preferred
    for j in range(len(column_values_cleaned)):
        for k in range(j + 1, len(column_values_cleaned)):
            if column_values_cleaned[j] > column_values_cleaned[k]:
                column_values_cleaned[j], column_values_cleaned[k] = column_values_cleaned[k], column_values_cleaned[j]

    # Calculate the avg number
    total = 0
    number_of_values = 0  # Using len(column_values_cleaned) would be preferred
    for value in column_values_cleaned:
        total += value
        number_of_values += 1
    average_number = total / number_of_values
    average_number = round(average_number, 2)

    # Output the result
    print(table_headers[i] + ' -> ' + str(column_values_cleaned[0]) + ' ' + str(column_values_cleaned[-1]) +
          ' ' + str(average_number))
