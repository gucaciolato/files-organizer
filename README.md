# files-organize

This program organizes files in a directory by extension. It does this by first creating a dictionary to map extension to directory. Then, it iterates through each file in the directory and checks if it is a regular file. If it is, it obtains the extension of the file and checks if it is already in the dictionary. If it is, it obtains the directory corresponding to the extension. If it is not, it creates the directory and adds it to the dictionary. Finally, it moves the file to the corresponding directory.

The program also calls itself recursively for each directory in the directory specified. This means that all files and subdirectories will be organized by extension.

The program is well-written and easy to understand. It is also efficient and effective.

Here are some specific details that you may want to include in your description:

The program uses the os module to interact with the operating system.
The program uses the sys module to get the platform of the operating system.
The program uses the os.listdir() function to iterate through the files in a directory.
The program uses the os.path.splitext() function to obtain the extension of a file.
The program uses the os.makedirs() function to create a directory.
The program uses the os.rename() function to move a file.
