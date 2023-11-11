def get_main_artist(artist):
    main_artist = artist.split("ft.", 1)[0].strip()
    return main_artist

def get_folder_structure_choice():
    user_input = input("Enter the custom folder structure using tags like {artist}/{album} (press Enter for default): ")
    return user_input.strip() if user_input.strip() else "{artist}/{album}"

def get_file_name_structure_choice():
    user_input = input("Enter the custom file name structure using tags like {track} - {artist} - {song} (press Enter for default): ")
    return user_input.strip() + "{extension}" if user_input.strip() else "{track} - {artist} - {song}{extension}"
