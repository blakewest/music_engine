import pandas as pd

class MusicEngine():
    def __init__(self):
        pass

    def run(self):
        df = pd.read_json(open('./data/all_my_loving.json'), orient="records")
        first_six_bars = df[:23]
        pitches, duration = first_six_bars['pitch'], first_six_bars['duration']
        pitch_patterns = self.find_pitch_patterns(pitches)
        rhythmic_pattern = self.find_rhythmic_pattern(duration)

    def find_rhythmic_pattern(self, durations):
        # This method should try to notice, for instance,
        # that a melody typically starts on the "and of 1",
        # or that it uses 16th notes, etc. Like.. it should try
        # to find *themes* within the rhythms
        # Prob just start with trying to find any one of those.

        # STEP 1 is to play around with the data in jupyter notebook
        pass

MusicEngine().run()

