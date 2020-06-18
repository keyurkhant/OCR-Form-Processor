file = open('text8.txt', 'r')
lines = file.readlines()

# Remove all content before first line of form
# This is required because there are many noice in image which are recognized as character by OCR.
firstIndex = lines.index('Cologuard Order Number:\n')

lines = lines[firstIndex:]

