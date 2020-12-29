# Cyberpunk Auto Crafter

Small python script to automate crafting in Cyberpunk - cuz
who's gonna keep clicking a thousand times....


## Installation

Clone the project anywhere and install all required dependencies
by running issuing the following command in the project's root
folder:

```bash
python -m pip install -r Requirements.txt
```

## Configuration

For now all configuration is done in the ```__main__.py``` directly.
One may configure the keys to press and the delays by editing
the following lines:

```python
clicker = Crafter(delay=.85)
presser = Disassembler(delay=.85, key='z', confirm='tab')
```

Simply set the delay to your configured crafting/disassembling 
delay (defaults are 0.8 seconds). I recommend adding a small extra
delay of 0.05 seconds or the game might not recognize your clicks.

You can also change the keybindings by editing the folowing lines
to your liking:

```python
keyboard.add_hotkey('f6', clicker.toggle)
keyboard.add_hotkey('f7', presser.toggle)
```

Simply change the strings ```'f6'``` & ```'f7'``` to your preferred
keyboard shortcut. 

## Running

Simply call the script by either calling the ```__main__.py```
directly or by executing the folder containing the ```__main__.py```
file. For example:

```bash
python __main__.py
```

Once the script is running press any of the hotkeys,
per default ```F6``` will start / stop the crafter
and ```F7``` will start / stop the disassembler.