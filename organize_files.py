import os
import downloads_dir

downloads_dir = downloads_dir.get_downloads_dir()

print(f'O caminho da pasta de downloads é: {downloads_dir}')


def organize_files_by_extension(downloads_dir):
    extension_to_dir = {}

    for root, dirs, files in os.walk(downloads_dir):
        for name in files:
            file_path = os.path.join(root, name)
            # Obtain the extension of the file
            _, file_extension = os.path.splitext(name)
            # remove the leading dot
            file_extension = file_extension[1:].lower()
            
            try:
                # verify if the extension is already in the dictionary
                if file_extension in extension_to_dir:
                    extension_dir = extension_to_dir[file_extension]
                else:
                    # create the directory if it doesn't exist
                    extension_dir = os.path.join(downloads_dir, file_extension)
                    os.makedirs(extension_dir, exist_ok=True)
                    extension_to_dir[file_extension] = extension_dir

                # move the file to the corresponding directory
                new_file_path = os.path.join(extension_dir, name)
                os.rename(file_path, new_file_path)
                print(f'Movendo "{name}" para "{extension_dir}"')
                
            except Exception as e:
                print(f"Erro ao processar o arquivo '{name}': {str(e)}")
