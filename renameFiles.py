import os 

folder_name = ""
directory = "./downloads/" + folder_name + "/"
name_files = "HOHO"
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir(directory): 
        dst = name_files + "_" + str(i) + ".jpg"
        src = directory + filename 
        dst = directory + dst 
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
