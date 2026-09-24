import csv
import json

file = open("Student.csv","w")

writer = csv.writer(file)
writer.writerow(["Roll_No","Name", "Marks"])
writer.writerow([1,"Dolly", "93"])
writer.writerow([2,"jack", "11"])
writer.writerow([3,"Saish", "100"])

file.close()

file = open("Student.csv", "r")
reader = csv.DictReader(file)
data = list(reader)

file.close()

file1 = open("output.json", "w")
json.dump(data, file1, indent=4)

file1.close()

print("CSV data converted to JSON successfully.")
