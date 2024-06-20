import re

input_file = open(r"C:\Users\UDESP\Downloads\Waveform1.txt")
output_file = open(r"C:\Users\UDESP\Downloads\Waveform1.txt", 'w')

for line in input_file:
    # Replace one or more spaces with a single comma
    # The plus sign in the regex pattern \s+ matches one or more whitespace characters
    new_line = re.sub(r'\s+', ',', line.strip())
    output_file.write(new_line + '\n')

input_file.close()
output_file.close()
