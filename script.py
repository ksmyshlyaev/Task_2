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
# TODO: remove: table_headers[0:2] = [' '.join(table_headers[0:2])]  # fixing the 'Def' 'Size' to 'Def Size'

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


print(table_data)
