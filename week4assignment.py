# #Question 1 file opening
# file = open("./week4 python class/input.txt","r")
# # print(file.read())

# # modified version
# writeDoc = open("./week4 python class/input.txt","a")
# writeDoc.write("\n This is an addittional text to my input, \n This should be on another line of the new document.")
# print(file.read())
# # New document
# newDoc = open("NewDoc.txt","w")
# newDoc.write("\n This is an addittional text to my input, \n This should be on another line of the new document.")

#Question 2 file handling
def read_file_with_error_handling():
    try:
        # Ask the user for a filename
        filename = input("./week4 python class/input.txt" )
        
        # Try to open and read the file
        with open("./week4 python class/input.txt", 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{"./week4 python class/input.txt"}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{"./week4 python class/input.txt"}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file_with_error_handling()




