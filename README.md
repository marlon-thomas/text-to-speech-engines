# Text-to-Speech Utility (powered by edge_tts)

Introducing Text-to-Speech Utility – powered by Edge TTS. This is a command-line utility that converts text from an input file to speech using a specified voice and saves it to an output audio file. It also provides an option to play the generated audio file immediately after creation.

When run without arguments, the utility displays help text along with a paginated list of available voices.


Why pay for expensive online services when you can harness the full power of text-to-speech technology for free? With the Edge TTS library, you can convert text into high-quality natural-sounding speech at no cost. Whether you're creating audiobooks, e-learning content, or adding voice to your apps, this utility brings professional-grade features without the price tag.

While many paid platforms offer text-to-speech services, this utility leverages the Edge TTS library that gives you all the features you need completely free for personal or commercial use. That means no subscription fees and no pay-per-use models. Just pure, high-quality speech generation at your fingertips.

Here are some examples of what you can do with this utility.

1. **Create Audiobooks for Free**: Turn your written content into immersive audiobooks and reach a wider audience—all without spending a cent.

2. **Develop engaging E-learning Content**: Enrich your tutorials, lessons, and presentations by adding clear engaging voice narration.

3. **Enhance Accessibility**: Make your websites, apps, and digital content more accessible to visually impaired users with spoken alternatives.

4. **Speak to a Global Audience**: Need multilingual content? Edge TTS supports multiple languages and accents to help you cater to diverse audiences, all without additional costs.

5. **Automate Voice Responses**: Save on expensive IVR systems by using this free utility to create professional-grade interactive voice responses.

6. **Generate Podcasts**: Convert your scripts into polished podcast episodes, with zero recording costs or studio time.

7. **Power Public Announcements**: Deliver important alerts, transit updates, or announcements with smooth, clear speech—all generated with this free tool.

## Features

- **Text-to-Speech Conversion**: Convert text from a file to speech using Microsoft Azure's Text-to-Speech voices via the `edge-tts` library.
- **Audio File Generation**: Save the generated speech to an audio file (e.g., MP3 format).
- **Optional Audio Playback**: Play the generated audio file after creation using the `--play` option.
- **Paginated Voice List**: Display a paginated list of available voices when no arguments are provided.

## Requirements

- **Python**: Version 3.7 or newer.

All dependencies are listed in the `requirements.txt` file:

- `edge-tts`: For text-to-speech conversion.
- `pygame` (optional): Required only if you want to play the audio using the `--play` option.

## Installation

### 1. Clone the Repository or Download the Script

Clone the repository:

```bash
git clone <repository_url>
```

Or download the `text_to_speech.py` script and the `requirements.txt` file from the repository.

### 2. Navigate to the Project Directory

```bash
cd <repository_directory>
```

### 3. Install Required Python Packages

Install the required Python packages using `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Using a Virtual Environment (Recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## Usage

```bash
./text_to_speech.py input_file output_file voice [--play]
```

- **`input_file`**: Path to the input text file containing the text you want to convert to speech.
- **`output_file`**: Path to the output audio file (e.g., `output.mp3`).
- **`voice`**: The voice to use for text-to-speech conversion. Use the `ShortName` of the voice.
- **`--play`** or **`-p`** (optional): Play the generated audio file after saving. Requires `pygame` to be installed.

### Examples

#### Convert Text to Speech Without Playing Audio

```bash
python ./text_to_speech.py ./input/input.txt output.mp3 "en-US-BrianMultilingualNeural"
```

#### Convert Text to Speech and Play Audio After Generation

```bash
python ./text_to_speech.py ./input/input.txt output.mp3 "en-US-BrianMultilingualNeural" --play
```

Or using the short option:

```bash
python ./text_to_speech.py ./input/input.txt ./output/output.mp3 "en-US-BrianMultilingualNeural" -p
```

## Displaying Available Voices

When you run the script without any arguments, it displays the help text and a paginated list of available voices.

```bash
python ./text_to_speech.py
```

**Output:**

```
usage: text_to_speech.py [-h] [input_file] [output_file] [voice] [--play]

Convert text from an input file to speech using a specified voice, and save it to an output file.

positional arguments:
  input_file   Path to the input text file
  output_file  Path to the output audio file (e.g., output.mp3)
  voice        Voice to use for text-to-speech

optional arguments:
  -h, --help   show this help message and exit
  --play, -p   Play the generated audio file after saving

Available Voices:
- en-US-AriaNeural: Female (English (United States))
- en-GB-RyanNeural: Male (English (United Kingdom))
- en-AU-NatashaNeural: Female (English (Australia))
... (more voices)
-- More -- (Press Enter to continue)
```

Press **Enter** to see more voices.

Use the **`ShortName`** (e.g., `en-GB-SoniaNeural`) when specifying the voice in the command.

## Voice Selection

The utility uses Microsoft Azure's Text-to-Speech voices available via the `edge-tts` library. Each voice has attributes such as `ShortName`, `Gender`, and `LocaleName`.

### Example Voices

- **English (United States)**
  - `en-US-AriaNeural`: Female
  - `en-US-GuyNeural`: Male

- **English (United Kingdom)**
  - `en-GB-SoniaNeural`: Female
  - `en-GB-RyanNeural`: Male

- **English (Australia)**
  - `en-AU-NatashaNeural`: Female
  - `en-AU-WilliamNeural`: Male

Use the **`ShortName`** when specifying the voice in the command.

## Dependencies

All dependencies are listed in the `requirements.txt` file.

### `requirements.txt` Contents

```
edge-tts
pygame  # Only required if you plan to use --play
```

If you do not need the audio playback feature, you can comment out or remove `pygame` from the `requirements.txt` file before installing.

## Troubleshooting

- **No Voices Displayed**:
  - Ensure that the `edge-tts` library is correctly installed and up to date:

    ```bash
    pip install --upgrade edge-tts
    ```

- **Python Version**:
  - Ensure you're using Python 3.7 or newer:

    ```bash
    python3 --version
    ```

- **`pygame` Not Installed**:
  - If you use the `--play` option without having `pygame` installed, you will receive an error message. Install `pygame`:

    ```bash
    pip install pygame
    ```

- **Permission Issues**:
  - Ensure you have read permissions for the input file and write permissions for the output directory.

- **Invalid Voice Name**:
  - If you specify a voice that doesn't exist, you may receive an error during the TTS conversion:

    ```
    Error during TTS conversion: The voice 'invalid-voice-name' is not available.
    ```

  - Run the script without arguments to see the list of available voices.

## Customization

- **Adjusting Pagination**:
  - The script paginates the list of available voices according to your terminal's height. You can adjust the number of lines displayed per page by modifying the `page_size` calculation in the script.

- **Changing the Prompt**:
  - You can change the prompt message displayed during pagination by editing the string in the `input()` function within the `paginate_output` function.

## License

This utility is released under the MIT License.

## Acknowledgments

- **edge-tts**: [GitHub Repository](https://github.com/rany2/edge-tts)
- **pygame**: [Official Website](https://www.pygame.org/)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

---
