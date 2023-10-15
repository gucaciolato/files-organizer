import os


def organize_files_by_extension(directory):
    # Create a dictionary to map extension to directory
    extension_to_dir = {}

    # Iterate through each file in the directory
    for name in os.listdir(directory):
        file_path = os.path.join(directory, name)

        if os.path.isfile(file_path):
            # Obtain the file extension
            _, file_extension = os.path.splitext(name)
            # remove the dot
            file_extension = file_extension[1:].lower()

            try:
                # verify if the extension is already in the dictionary
                if file_extension in extension_to_dir:
                    extension_dir = extension_to_dir[file_extension]
                else:
                    # create the directory
                    extension_dir = os.path.join(directory, file_extension)
                    os.makedirs(extension_dir, exist_ok=True)
                    extension_to_dir[file_extension] = extension_dir

                # move the file
                new_file_path = os.path.join(extension_dir, name)
                os.rename(file_path, new_file_path)
                print(f'Movendo "{name}" para "{extension_dir}"')

            except Exception as e:
                print(f"Erro ao processar o arquivo '{name}': {str(e)}")

        elif os.path.isdir(file_path):
            # if a directory, recursively call the function
            organize_files_by_extension(file_path)
