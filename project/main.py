#!/usr/bin/env python3

"""
Basic example of edge_tts usage.
"""

import asyncio
import pygame
import edge_tts

'''
$ edge-tts --list-voices | grep en-
Name: en-AU-NatashaNeural
Name: en-AU-WilliamNeural
Name: en-CA-ClaraNeural
Name: en-CA-LiamNeural
Name: en-GB-LibbyNeural
Name: en-GB-MaisieNeural
Name: en-GB-RyanNeural
Name: en-GB-SoniaNeural
Name: en-GB-ThomasNeural
Name: en-HK-SamNeural
Name: en-HK-YanNeural
Name: en-IE-ConnorNeural
Name: en-IE-EmilyNeural
Name: en-IN-NeerjaExpressiveNeural
Name: en-IN-NeerjaNeural
Name: en-IN-PrabhatNeural
Name: en-KE-AsiliaNeural
Name: en-KE-ChilembaNeural
Name: en-NG-AbeoNeural
Name: en-NG-EzinneNeural
Name: en-NZ-MitchellNeural
Name: en-NZ-MollyNeural
Name: en-PH-JamesNeural
Name: en-PH-RosaNeural
Name: en-SG-LunaNeural
Name: en-SG-WayneNeural
Name: en-TZ-ElimuNeural
Name: en-TZ-ImaniNeural
Name: en-US-AnaNeural
Name: en-US-AriaNeural
Name: en-US-ChristopherNeural
Name: en-US-EricNeural
Name: en-US-GuyNeural
Name: en-US-JennyNeural
Name: en-US-MichelleNeural
Name: en-US-RogerNeural
Name: en-US-SteffanNeural
Name: en-ZA-LeahNeural
Name: en-ZA-LukeNeural
'''
#VOICE = "en-US-ChristopherNeural"
#VOICE="en-NG-AbeoNeural"
#VOICE="en-TZ-ImaniNeural"
#VOICE="en-GB-LibbyNeural"
#VOICE="en-GB-SoniaNeural"
#VOICE="en-US-MichelleNeural"
#VOICE="en-US-RogerNeural"
VOICE="en-US-SteffanNeural"

OUTPUT_FILE = "output/output.mp3"

async def speak(data) -> None:
    #command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    #os.system(command)
    communicate = edge_tts.Communicate(data, VOICE)
    await communicate.save(OUTPUT_FILE)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output/output.mp3")

    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        # Open the file and ignore invalid characters
        with open('input/input.txt', 'r', encoding='utf-8', errors='ignore') as f:
            input_text = f.read().replace('\n', ' ').replace('\r', ' ')
        # Replace newline characters with spaces
        loop.run_until_complete(speak(input_text))
    finally:
        loop.close()