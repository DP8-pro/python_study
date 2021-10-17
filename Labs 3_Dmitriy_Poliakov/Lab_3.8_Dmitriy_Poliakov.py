# Write a script that creates a new output file called myfile.txt
f = open('myfile.txt','w')

# Write into file string "Hello file world!"
f.write("Hello file world!")

# Close file
f.close()

# Create file object for above file with mode “r+”
f = open('myfile.txt','r+')

# Read and print file content
print(f.read())

# Move to string position after Hello and set new value here
f.seek(len("Hello "))

# Save file with flush method
f.write("my " + "file world!")
f.flush()
