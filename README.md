# Encodid Source Code
This is the source code for Encodid and the stable, released version can be found [here](https://github.com/TomTheCatt/Encodid). Encodid is a program built with only one goal: make every message impossible to decode no matter what resources were avaliable. Encodid accomplished exactly that.

Encodid uses a series of all characters in a random sequence of 4 through 22. Around 96 characters are used in the sequence, including whitespaces and backlashes.

### Install
1. Download the code from the repository as a `.zip` file. Extract all contents to a desired location.
2. Run `rewrite_key.py`. The key is currently a "0", and needs to be updated. `rewrite_key.py` takes care of this.
3. Run `main.py` and enter a string of `Encodid` encrypted data or a regular sentence. `main.py` will automatically decode or encode the sequence depending on the input.

**NEEDED PYTHON MODULES**

Pickle, Colorama 

### Keys
To create a new key, simply ensure that `key.txt` file exists in the same directory as `rewrite_key.py`, and then run `rewrite_key.py`.

To share a key, simply upload a copy of your `key.txt` file and others will download it. To install a shared key, simply delete `key.txt` and replace it with the new key. Rename the new key and it's extension to `key.txt`.

### Uninstall
Simply delete the file and all of it's contents.
