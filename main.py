import os
from organizer import organize_music
from utils import get_folder_structure_choice, get_file_name_structure_choice

if __name__ == "__main__":
    music_directory = input("Enter the path to your music directory: ")

    folder_structure = get_folder_structure_choice()

    file_name_structure = get_file_name_structure_choice()
    
    if os.path.exists(music_directory):
        log_file = os.path.join(music_directory, 'log.txt')
        
        organize_music(music_directory, log_file, folder_structure, file_name_structure)
        print(f"Organizing and renaming completed successfully. Log written to {log_file}")
    else:
        print("The entered directory does not exist. Please provide a valid path.")