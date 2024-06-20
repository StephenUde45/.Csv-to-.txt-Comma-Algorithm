# Import the regular expression module
import re

# Open the input file for reading. The 'r' before the string starts a raw string literal,
# which tells Python to treat backslashes as literal characters.
input_file = open(r"C:\Users\UDESP\Downloads\Waveform1.txt", 'r')

# Open the output file for writing. Please note that the path provided should be different
# from the input file to prevent overwriting the original file with the new, comma-separated version.
# The following line should have a different filename or path for the output to prevent data loss.
output_file = open(r"C:\Users\UDESP\Downloads\Waveform1_with_commas.txt", 'w')

# Iterate over each line in the input file
for line in input_file:
    # Use a regular expression to replace sequences of whitespace (spaces, tabs, etc.)
    # with a single comma. The function strip() is used to remove any leading
    # and trailing whitespace from the line before processing it.
    new_line = re.sub(r'\s+', ',', line.strip())
    
    # Write the modified line to the output file, adding a newline character at the end
    # to ensure that each line is properly separated in the output file.
    output_file.write(new_line + '\n')

# Close the input file to free up system resources
input_file.close()

# Close the output file to ensure that all data is written to disk
output_file.close()
