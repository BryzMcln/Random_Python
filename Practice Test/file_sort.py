import os
import shutil


def create_folders(directory, file_types):
    folders = ["Documents", "Photos", "Sounds", "Video", "Codes", "Others"]

    for folder in folders:
        extensions = file_types.get(folder, [])
        folder_path = os.path.join(directory, folder)

        # Check if there are files that meet the requirements for the current folder
        files_exist = any(
            any(ext.lower() in filename.lower() for ext in extensions)
            for filename in os.listdir(directory)
        )

        if files_exist and not os.path.exists(folder_path):
            os.makedirs(folder_path)


def organize_files(directory, file_types):
    counts = {folder: 0 for folder in file_types.keys()}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination_folder = os.path.join(directory, folder)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    counts[folder] += 1
                    break

    return counts


if __name__ == "__main__":
    input_directory = input("Enter the directory path: ")

    if os.path.exists(input_directory):
        file_types = {
            "Documents": [".docx", ".pptx", ".csv", ".xlsx", ".pdf"],
            "Photos": [".svg", ".webp", ".jpeg", ".jpg", ".png", ".vector", ".gif"],
            "Sounds": [".mp3", ".wav", ".m4a", ".wma"],
            "Video": [".mp4", ".mkv", ".avi", ".wmv", ".webm"],
            "Codes": [
                ".py",
                ".json",
                ".js",
                ".php",
                ".html",
                ".css",
                ".mwb",
                ".sql",
                ".db",
                ".bak",
                ".txt",
            ],
            "Others": [".rar", ".apk", ".zip"],
        }

        create_folders(input_directory, file_types)
        counts = organize_files(input_directory, file_types)

        print("Files have been sorted successfully.")
        for folder, count in counts.items():
            if count > 0:
                print(f"{folder}: {count} files")
            else:
                print(f"{folder}: No files")
    else:
        print("Invalid directory path. Please provide a valid path.")
