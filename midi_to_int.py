import math
from music21 import *
import os
import numpy as np
from midi_note import MIDINote
import json



class MIDINote:

    def __init__(self, note, duration_type, length):
        self.note = note
        self.duration_type = duration_type
        self.length = length
        self.as_map = {
            "note": note,
            "duration_type": duration_type,
            "length": length
        }

def parse_raw_notes(file_path):
    print("Loading Music File:", file_path)
    raw_notes = []
    midi_data = converter.parse(file_path)
    for part in midi_data.parts:
        print(part.partName)
        if part.partName == 'MELODY':
            midi_elements = part.recurse()
            for element in midi_elements:
                if isinstance(element, note.Note):
                    note_duration = duration.Duration()
                    note_duration.quarterLength = element.quarterLength
                    raw_note = str(element.pitch)
                    raw_notes.append(MIDINote(raw_note, str(note_duration.type), str(element.quarterLength)).as_map)
    return raw_notes

PATH = "./Varied Rhythm/"
filenames = os.listdir(PATH)
preset_paths = [PATH + filename for filename in filenames]

parsed_midi_notes = []
for song_path in preset_paths:
    parsed_raw_notes = parse_raw_notes(song_path)
    parsed_midi_notes.append(parsed_raw_notes)

print(parsed_midi_notes)