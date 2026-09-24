# Input file
file = open("Input.txt","w")
file.write("Name: Saish Mangale")
file.write("\nDiv: SY-1")
file.write("\nBatch: B")
file.write("\nDepartment: CSE")

file.close()

# Counting no of rows
file = open("Input.txt","r")
lines = file.readlines()
count = 0
for line in lines:
    count += 1
print("No of lines in file: ",count)

first_two_lines = lines[:2]
file.close()

#Writing 1st 2 lines in Output file
file2 = open("Output.txt","w")
for line in first_two_lines:
    file2.write(line)
file2.close()

print("2 lines extarcted to Output file from Input file")
