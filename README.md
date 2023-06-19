# Silence Broken By

This project plays a random sound at random intervals. Pretty fun, right?

# How it works

Every second, the program rolls to see if it will play something. If the roll is successful, it will play a random file from the ones specified in [config.json](config.json). The chance for success for every roll is also located in [config.json](config.json), with the key "odds".

## How to use

Just download the latest release from the side and run `start.bat`. It's that easy.

## How to contribute

Feel free to contribute however you want, be it code or new sounds.

### Sounds

1. Fork the repository
2. Clone the repository
3. Open `config.json`
4. Look for `"sounds"`
5. Add a key-value pair in the following format: `"name": "sounds/filename"`. Acceptable extension are MP3 and WAV
6. Add the sound file to the `sounds` directory
7. Commit, push, and create a pull request

### Code

1. Fork the repository, then clone it
2. If you do not have python installed, go to https://www.python.org/ and download it
3. Open your editor, and a terminal in your working directory
4. Run the following command to create a virtual environment
    py -m venv .venv
5. Activate the virtual environment with one of these commands
    - For Windows, Powershell use `.venv\Scripts\Activate.ps1`
    - For Windows, Command Prompt use `.venv\Scripts\Activate.bat`
6. Run the following command to install required modules
    pip install "requirements.txt"
7. Add your contributions
8. Commit, push and create a pull request

