
A super simple command line snippet display script.

Any snippets etc you want at hand go into a txt file in `/thoughts`.

### Setup:
* have python3 installed.
* clone this repo
* add an alias to pull the latest repo and run the `check_brain.py` script
eg `alias brain="git -C /home/mike/mikeAdamss/brain pull && python3 /home/mike/mikeAdamss/brain/check_brain.py"`

### Usage:
`brain` will list all the tags for all thoughts, along with a count of their occurances.

`brain <tag>` or `brain <tag> <tag>` (for ,pre precise results) will return you the text from `/thoughts` with a bit of friendly colour.


### Adding Snippets:
* Stick em in the `/thoughts` repo (on your own branch presumably).