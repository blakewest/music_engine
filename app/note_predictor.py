import numpy as np
from scipy import signal
from music21.note import Note

class NotePredictor():
    def __init__(self):
        pass

    def next_note(self, notes):
        """
        notes: Music21 Stream or list of ints/floats
        returns: Musci21 Note
        """
        note_numbers = notes if isinstance(notes[0], (int, float)) else list(map(lambda note: note.pitch.ps, notes.flat.getElementsByClass('Note')))
        pattern = self.find_best_pattern(note_numbers)
        print("Best pattern found is:", pattern)
        note_number = self.next_note_from_pattern(note_numbers, pattern)
        return Note(note_number)

    def find_best_pattern(self, note_numbers):
        diff = np.diff(note_numbers)
        pattern_options = range(1, max(len(diff), 2))
        conv_scores = [np.sum(self.conv_1d(diff, diff[:i], stride=i)) for i in pattern_options]
        return diff[:(np.argmax(conv_scores) + 1)]

    def next_note_from_pattern(self, note_numbers, pattern):
        last_part_of_pattern_used = len(note_numbers) % len(pattern)
        next_part_of_pattern = (last_part_of_pattern_used + 1) % len(pattern)
        return note_numbers[-1] + pattern[next_part_of_pattern]

    def conv_1d(self, notes, pattern, stride=1):
        convolved = signal.fftconvolve(notes, pattern[::-1], mode='valid')
        # This only returns certain indexes to mimic if scipy directly
        # supported strided convolutions. It's a hack, but a perfectly legit one.
        idx_to_take = np.arange(0, convolved.shape[0], stride)
        return convolved[idx_to_take]

# stream = converter.parse("tinyNotation: 4/4 c4 d4 e4")
# NotePredictor().predict_next(stream)
# --> returns Music21Stream[60, 62, 64, 66]
