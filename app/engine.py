import pandas as pd
import random
from music21 import midi, note

class MusicEngine():
    def __init__(self):
        pass

    def run(self, filename, melody_track=1):
        midi_file = self.open_midi_file(filename)
        stream = midi.translate.midiFileToStream(midi_file)
        melody = stream.parts[melody_track]
        new_melody = self.suggest_new_melody(melody)
        player = midi.realtime.StreamPlayer(new_melody)
        print("Playing the new melody")
        player.play()

    def suggest_new_melody(self, melody):
        snippet = melody[:30]
        options = self.analyze_melody(snippet)
        snippet.append(random.sample(options, 1)[0])
        return snippet

    def analyze_melody(self, melody, strategy="same_direction"):
        print("Analyzing...")
        for note_obj in melody:
            # Do stuff with note.pitch or something
            pass
        return [note.Note("B6", type="whole"), note.Note("B3", type="whole")]

    def open_midi_file(self, filename):
        print("Opening file...")
        mf = midi.MidiFile()
        mf.open(filename)
        mf.read()
        return mf

    def find_rhythmic_pattern(self, durations):
        # This method should try to notice, for instance,
        # that a melody typically starts on the "and of 1",
        # or that it uses 16th notes, etc. Like.. it should try
        # to find *themes* within the rhythms
        # Prob just start with trying to find any one of those.

        # STEP 1 is to play around with the data in jupyter notebook
        pass

MusicEngine().run('./all_my_loving.midi')
