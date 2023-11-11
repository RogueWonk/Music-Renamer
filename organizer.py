import os, shutil, datetime
from tinytag import TinyTag
from utils import get_main_artist

def organize_music(directory, log_file, folder_structure, file_name_structure):
    with open(log_file, 'w') as log:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.mp3', '.flac', '.ogg', '.wav')):
                    file_path = os.path.join(root, file)
                    tag = TinyTag.get(file_path)

                    main_artist = get_main_artist(tag.artist) if tag.artist else "Unknown Artist"
                    album = tag.album if tag.album else "Unknown Album"

                    dynamic_folder_structure = folder_structure.replace("{artist}", main_artist).replace("{album}", album)
                    directory_structure = os.path.join(directory, dynamic_folder_structure)
                    os.makedirs(directory_structure, exist_ok=True)

                    new_file_name = file_name_structure.format(
                        track=int(tag.track) if tag.track else 0,
                        artist=main_artist,
                        song=tag.title if tag.title else "Unknown Song",
                        extension=os.path.splitext(file)[1]
                    )

                    new_file_path = os.path.join(directory_structure, new_file_name)
                    shutil.move(file_path, new_file_path)

                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_entry_folder = f"{timestamp} - Created folder: {directory_structure}\n"
                    log.write(log_entry_folder)

                    log_entry_file = f"{timestamp} - Renamed file: {new_file_name}\n"
                    log.write(log_entry_file)

    with open(log_file, 'a') as log:
        for root, dirs, _ in os.walk(directory, topdown=False):
            for dir_name in dirs:
                folder_path = os.path.join(root, dir_name)
                if not os.listdir(folder_path):
                    os.rmdir(folder_path)

                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_entry = f"{timestamp} - Deleted empty folder: {folder_path}\n"
                    log.write(log_entry)
