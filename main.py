import downloads_dir
import organize_files_by_extension


if __name__ == '__main__':
    downloads_dir = downloads_dir.get_downloads_dir()
    organize_files_by_extension = organize_files_by_extension.organize_files_by_extension(
        downloads_dir)
