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
        new_note = random.sample(options, 1)[0]
        print("Appending", new_note)
        snippet.append(new_note)
        return snippet

    def analyze_melody(self, melody, strategy="same_direction"):
        print("Analyzing...")
        last_two_notes = list(filter(lambda n: isinstance(n, note.Note), melody))[-2:]
        last_pitch = last_two_notes[-1].pitch.ps
        last_movement = last_two_notes[-1].pitch.ps - last_two_notes[0].pitch.ps
        return [note.Note(last_pitch + last_movement, type="whole"), note.Note(last_pitch - last_movement, type="whole")]

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
