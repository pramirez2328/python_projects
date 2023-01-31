import os

absolute_path = os.path.dirname(__file__)
relative_path = "../week3/my_file.txt"
reading_path = os.path.join(absolute_path, relative_path)
write_path = os.path.join(absolute_path, "../week3/output.txt")

# Create a file

my_file2 = open(reading_path, 'r')
output = open(write_path, 'a+')
for line in my_file2:
    print(line.strip(), file=output)

print('This is a new line', file=output)

my_file2.close()
output.close()
