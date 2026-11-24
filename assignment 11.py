# Open a file in write mode and write data
file = open("sample.txt", "w")
file.write("Hello, this is the first line in the file.\n")
file.write("File handling in Python is easy to learn.\n")
file.close()  # Closing the file
print("Data written successfully.\n")

# Open the file in read mode and display contents
file = open("sample.txt", "r")
print("Reading file contents:")
content = file.read()
print(content)
file.close()

# Step 3: Open the file in append mode and add more data
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.close()
print("\nData appended successfully.\n")

# Read the file again to see updated content
file = open("sample.txt", "r")
print("Updated file contents:")
print(file.read())
file.close()
