# Cyberpunk Auto Crafter

Small python script to automate crafting in Cyberpunk - cuz
who's gonna keep clicking a thousand times.... Just run CAC and
go enjoy yourself a nice cup of tea :D

## Prerequisites

Python 3 is required for CAC to run, you can download the latest
version [here](https://www.python.org/). Just follow the installation
steps.


## Setup

Clone the project anywhere and install all required dependencies
by running issuing the following command in the project's root
folder:

```bash
python -m pip install -r Requirements.txt
```

## Configuration

If you have not messed around with your keyboard shortcuts or
the delays you can just run the program as is. If you did follow
these steps to configure CAC.

For now all configuration is done in the ```__main__.py``` directly.
One may configure the keys to press and the delays by editing
the following lines:

```python
clicker = Crafter(delay=.85)
presser = Disassembler(delay=.85, key='z', confirm='tab')
```

Simply set the delay to your configured crafting/disassembling 
delay (defaults are 0.8 seconds), instructions on how to change 
the delays can be found [here](https://www.nexusmods.com/cyberpunk2077/mods/152).
I played around with the delay a bunch and recommend adding a small extra delay of 0.05
seconds to your configured delay or the game might not finish crafting / disassembling 
your item.

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