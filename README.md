### Music Engine
The music engine is an application that takes in MIDI, and can output ideas on where to go next, or tell you what parts are interesting, or ear catching within a piece. If you play a simple melody, it will suggest ways to extend or vary that melody.

### How to use
You can start by playing a simple melody on piano, recording it as a MIDI file, uploading that to the Engine, and then wait the Engine will output an extension, or variations on that melody.

### Demo
If you want, you can run `python app/engine.py`

### Getting Started With The Repo
  - Install `conda` if you have not. Go [here](https://www.continuum.io/downloads) to do that. It is a package manager, as well as an data-science optimized version of Python.
  - Once installed, make sure you're in the root directory of this project (eg. ~/code/music_engine), and type `conda env create` at your command line. This will install all the packages.

### Developing
  - If you install new packages, make sure to run `conda env export > environment.yml`, which will automatically detect your new package, and save it to the environment.yml file.

  - To update from a new package install, do `conda env update`

  - To add new features/ideas, just make a branch, and then PR it.

  - I'm actiavely soliciting ideas for where to take this project! Right now it's vague, and I need help!
