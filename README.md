# Files Organizer
This program organizes files in a directory by extension.

## Summary
The program works by first creating a dictionary to map extension to directory. Then, it iterates through each file in the directory and checks if it is a regular file. If it is, it obtains the extension of the file and checks if it is already in the dictionary. If it is, it obtains the directory corresponding to the extension. If it is not, it creates the directory and adds it to the dictionary. Finally, it moves the file to the corresponding directory.

The program also calls itself recursively for each directory in the directory specified. This means that all files and subdirectories will be organized by extension.

## How to use
To use the program, simply run the following command:

```bash
python main.py
```

## Additional details
### The program uses the following modules:

- os to interact with the operating system
- sys to get the platform of the operating system

### The program uses the following functions:

- os.listdir() to iterate through the files in a directory
- os.path.splitext() to obtain the extension of a file
- os.makedirs() to create a directory
- os.rename() to move a file

## License
This program is licensed under the MIT License.

## Author
This program was created by Gu Caciolato.
