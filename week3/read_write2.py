import os

absolute_path = os.path.dirname(__file__)
relative_path = "../week3/src_input/in_file2.txt"
reading_path = os.path.join(absolute_path, relative_path)
write_path = os.path.join(absolute_path, "../week3/src_output/out_file2.txt")
read_file = open(reading_path, 'r')
output = open(write_path, 'a+')

for line in read_file:
    print(line.strip(), file=output)

read_file.close()
output.close()
