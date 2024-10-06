#!/usr/bin/env python3

"""
Command-line utility that converts text from an input file to speech using a specified voice,
and saves it to an output file. When run without arguments, it displays help text along with
a list of available voices, paginated according to the terminal height.

Usage:
    ./text_to_speech.py input.txt output.mp3 "en-GB-SoniaNeural" [--play]
"""

import os  # Import os at the top
# Suppress the pygame welcome message by setting the environment variable before importing pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import argparse
import asyncio
import sys
import shutil
import importlib
import edge_tts
from tqdm import tqdm  # For the progress bar
import contextlib
import io

# Import pygame after setting the environment variable
try:
    import pygame
except ImportError:
    pygame = None  # Handle the case where pygame is not installed

async def get_voice_list():
    voices = await edge_tts.list_voices()
    return voices

async def speak(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)

        # Count total number of words in the input text
        total_words = len(text.split())
        if total_words == 0:
            print("Input text is empty.")
            return

        # Initialize the progress bar with the total number of words
        pbar = tqdm(total=total_words, desc='Encoding', unit='word', leave=True)

        # Open the output file for writing
        with open(output_file, 'wb') as audio_file:
            # Start the TTS conversion and stream the results
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    data = chunk["data"]
                    audio_file.write(data)
                elif chunk["type"] == "WordBoundary":
                    pbar.update(1)
            pbar.close()
            print("\nEncoding complete.")
        print(f"Audio has been saved to {output_file}")
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        return

def play_audio_file(output_file):
    if pygame is None:
        print("Error: 'pygame' is not installed. Please install it to use the --play option.")
        return

    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        print("Playing audio...")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error during audio playback: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

def paginate_output(lines):
    # Get terminal size
    terminal_size = shutil.get_terminal_size((80, 24))
    page_size = terminal_size.lines - 3  # Leave room for prompt and avoid zero or negative

    # Paginate the lines
    total_lines = len(lines)
    current_line = 0
    while current_line < total_lines:
        # Calculate the end line for the current page
        end_line = min(current_line + page_size, total_lines)
        # Display the current page
        for line in lines[current_line:end_line]:
            print(line)
        current_line = end_line
        # If there are more lines, prompt the user
        if current_line < total_lines:
            input("-- More -- (Press Enter to continue)")
        else:
            break

def main():
    parser = argparse.ArgumentParser(
        description="Convert text from an input file to speech using a specified voice, and save it to an output file."
    )
    parser.add_argument("input_file", nargs='?', help="Path to the input text file")
    parser.add_argument("output_file", nargs='?', help="Path to the output audio file (e.g., output.mp3)")
    parser.add_argument("voice", nargs='?', help="Voice to use for text-to-speech")
    parser.add_argument(
        "--play", "-p", action="store_true",
        help="Play the generated audio file after saving"
    )

    # Check if no arguments are supplied
    if len(sys.argv) == 1:
        # No arguments provided; display help text and available voices
        loop = asyncio.get_event_loop()
        voices = loop.run_until_complete(get_voice_list())
        parser.print_help()
        print("\nAvailable Voices:")
        voice_lines = []
        for voice in voices:
            short_name = voice.get('ShortName', 'Unknown ShortName')
            gender = voice.get('Gender', 'Unknown Gender')
            locale_name = voice.get('LocaleName', voice.get('Locale', 'Unknown Locale'))
            voice_lines.append(f"- {short_name}: {gender} ({locale_name})")
        paginate_output(voice_lines)
        sys.exit()

    args = parser.parse_args()

    # Ensure all required arguments are provided
    if not args.input_file or not args.output_file or not args.voice:
        parser.error("the following arguments are required: input_file, output_file, voice")

    # Read the input text file, ignoring invalid characters
    try:
        with open(args.input_file, 'r', encoding='utf-8', errors='ignore') as f:
            input_text = f.read().replace('\n', ' ').replace('\r', ' ')
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Run the speak function asynchronously to encode and save the file
    try:
        asyncio.run(speak(input_text, args.voice, args.output_file))
    except Exception as e:
        print(f"Error in asyncio event loop: {e}")

    # If the --play option is specified, play the audio file
    if args.play:
        play_audio_file(args.output_file)

if __name__ == "__main__":
    main()
