# COTL Music Player

The COTL Music Player is a Python-based application designed to play music in Sky: Children of The Light through simulated keyboard inputs. It reads musical notes from JSON files and plays them by pressing keys according to the notes' timings and sequences. This project is inspired by the in-game music sheets and aims to provide a fun and interactive way to practice and enjoy music in game.

![demo](./media/demo.mp4)

## Features

- **Song Selection**: Users can choose from a variety of songs listed in the `songs` directory. Each song is stored in a JSON file, which contains the notes and timings for the song.
- **Playback Control**: During playback, users can pause and resume the song using keyboard shortcuts. This feature adds flexibility, allowing users to take breaks or skip parts of the song as needed.
- **Dynamic Song Loading**: The application dynamically loads the song selected by the user, ensuring that only the chosen song is in memory during playback.
- **Progress Display**: As the song plays, the application displays a progress bar, giving users a visual indication of how much of the song has been played and how much is left.

## How It Works

1. **Song Selection**: Upon starting, the application prompts the user to select a song from the available options in the `songs` directory. The selection is made through a user-friendly interface that lists all the songs by title.
2. **Song Loading**: After selection, the application loads the song data from the corresponding JSON file. This data includes the notes of the song and their respective timings.
3. **Playback**: The application waits for the user to initiate playback by pressing a specific key. Once started, it simulates keyboard inputs based on the notes and timings defined in the song data. The playback can be paused, resumed, or stopped by the user at any time.
4. **Completion**: When the song ends, the application notifies the user that the song is complete. The user can then choose to play the same song again or select a new one.

## Getting Started

To use the COTL Music Player, follow these steps:

1. Ensure you have Python installed on your computer.
2. Clone or download this repository to your local machine.
3. Navigate to the project directory in your terminal or command prompt.
4. Run `main.py` using Python to start the application.
5. Click enter to select a song, (arrow keys to navigate)
6. Press `\` to start the song playback.
7. Press `-` to pause, and `=` resume the song playback.
8. Press `backspace` to stop the song and choose another.

Enjoy the music!