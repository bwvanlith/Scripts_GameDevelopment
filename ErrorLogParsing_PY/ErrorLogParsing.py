

# Input filename or default name if none is entered
destination_file = input("Enter filename to process: ")
my_text = open(destination_file, "r")
problem_asset = ""
output_file = open("filtered_output.txt", "w")
filter_phrase = input("Enter a word or phrase to filter: ")
for line in my_text:
    if filter_phrase in line:
        output_file.write(line)
    elif filter_phrase in line:
        output_file.write(line)
my_text.close()
output_file.close()
print(destination_file + " was successfully processed to filtered_output.txt")

# If file doesnt exist
print("file does not exist")

# If word or phrase isn't found
print("word or phrase not found")

