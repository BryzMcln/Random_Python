import zipfile, os
import time

def clear():
    os.system('cls')

def display_compression_levels():
    print("Available Compression Levels:")
    print("=============================")
    print("1. No Compression")
    print("2. Low Compression")
    print("3. Medium Compression")
    print("4. High Compression")
    print("=============================")

def get_valid_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print("=============================")
            print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("=============================")
            print("Please enter a valid integer.")

def get_yes_or_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("=============================")
            print("Please enter 'y' or 'n'.")

def compression_level():
    display_compression_levels()
    print("=============================")
    lvl = get_valid_integer_input("Enter the Compression Level (1-4): ", 1, 4)
    directory = input("Enter the Directory: ")
    filename = input("Enter file name: ")

    if not os.path.isdir(directory):
        print("=============================")
        print("Invalid directory. Please enter a valid directory path.")
        return

    if not os.listdir(directory):
        print("=============================")
        print("Directory is empty. No files to compress.")
        return

    # Create a zip file with the given filename
    zip_filename = f"{filename}.zip"
    zip_file = zipfile.ZipFile(zip_filename, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=lvl)

    # Add all files in the given directory to the zip file
    for foldername, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path, arcname=os.path.relpath(file_path, directory))

    # Close the zip file
    zip_file.close()

    # Ask the user if they want to delete the files after compression
    delete_files = get_yes_or_no_input("Do you want to delete the files after compression? (y/n): ")

    if delete_files:
        # Delete the files
        for foldername, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
    print("=============================")
    print("Compression completed.")
    print("Waiting...")
    time.sleep(2)  # Add a 2-second delay before exiting

if __name__ == '__main__':
    compression_level()
