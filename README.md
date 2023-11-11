# Music Renamer 

  

The **Music Renamer** script is a Python tool designed to organize and rename music files in a specified directory based on their metadata. It utilizes the `TinyTag` library to extract metadata information from music files (MP3, FLAC, OGG, WAV) and organizes them into folders named by artist and album.

  

## Features

  

-  **Organize by Artist and Album:** Automatically creates folders named after the artist and album and organizes music files accordingly.

  

-  **Customizable File Naming:** Users can customize the file naming structure using placeholders such as `{track}`, `{artist}`, `{song}`, etc.

  

-  **Automatic Handling of Featured Artists (ft):** The script extracts the main artist from the metadata, ignoring featured artists.

  

-  **Logging:** The script generates a log file (`log.txt`) that records the created folders and renamed files, including timestamps.

  

-  **Cleanup:** Automatically deletes any empty folders left after organizing the music files.

  

## Usage

  

1.  **Clone the Repository:**
	```bash
	git clone https://github.com/roguewonk/music-renamer.git
	cd music-renamer
	```

2.  **Install Dependencies:**
	```bash
	pip install TinyTag
	```

3. **Run the Script:**
	```bash
	python main.py
	```

4.  **Follow the Prompts:**  
- Enter the path to your music directory. 
- Choose the folder structure (or press Enter for default). 
- Choose the file name structure (or press Enter for default). 

5.  **Review the Log:**  
- Check the generated log file (`log.txt`) for a record of the organized folders and renamed files.

## Customizing Folder Naming 
By default, the script organizes music files into folders named after the artist and album. You can customize the folder naming structure using placeholders: 
-  **Default Structure:**  `{artist}/{album}`  

-  **Available Placeholders:**  
	-  `{artist}`: Main artist (ignores featured artists). 
	-  `{album}`: Album name. 
	
-  **Example:** 
User enters a custom folder structure: `{artist}/{album}`  
	-  Original file: `01 - Artist feat. Another Artist - Song Title.mp3`  
	-  Renamed file: `Artist - Song Title - Track 01.mp3`  
	-  Folder created: `Artist/Album Name`  

## Customizing File Naming

- **Default Structure:** `{track} - {artist} - {song}`

- **Available Placeholders:**
  - `{track}`: Track number (padded with zeros).
  - `{artist}`: Main artist (ignores featured artists).
  - `{song}`: Song title.
  - `{extension}`: Original file extension. 
	  - *This is included automatically in the file name, but may be manually defined. If this tag is not defined the script will automatically add it.*

- **Example:**

  User enters a custom file name structure: `{artist} - {song} - Track {track}`

  - Original file: `01 - Artist feat. Another Artist - Song Title.mp3`
  - Renamed file: `Artist - Song Title - Track 01.mp3`

## Contributing 
Contributions are welcome! Here's how you can contribute to the project: 
1. Fork the repository on GitHub. 

2. Clone your forked repository to your local machine: 
	```bash 
	git clone https://github.com/roguewonk/music-renamer.git 
	cd music-renamer 
	```

3. Create a new branch for your changes: 
	```bash 
	git checkout -b feature/your-feature-name 
	``` 

4. Make your changes and test them thoroughly. 

5. Commit your changes: 
	```bash 
	git add . 
	git commit -m "Add your meaningful commit message here" 
	```
 
6. Push your changes to your fork on GitHub: 
	```bash 
	git push origin feature/your-feature-name 
	``` 

7. Open a pull request (PR) against the original repository. 

8. Provide a clear and detailed description of your changes in the PR. 

9. Your PR will be reviewed, and once accepted, it will be merged into the main branch. 
 
### Code Style  

- Please adhere to the existing code style in the project. 
- If you're introducing a new feature, consider adding relevant documentation and tests. 

### Contributor License Agreement (CLA) 

By submitting a contribution (pull request, issue, comment, or any other form of contribution) to this project, you agree to the following: 

1. You grant the maintainers of the Music Renamer project a non-exclusive, irrevocable, worldwide, royalty-free license to use, reproduce, modify, sublicense, distribute, and make derivative works of your contribution. 

2. You assert that you have the right to grant the above license and that your contribution does not violate any third-party rights. 

3. You understand and agree that your contribution may be publicly disclosed.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.
