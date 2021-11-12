# goodMorning.py

This is a simple "smart" alarm clock script written in Python. It's currently in its early stages but I'm hoping to add more customization and a better user interface.

---

## Setup and installation

There are a couple of libraries that need to be installed in order for the base code to run.

* pyttsx3 - text-to-speech library
* CoinGeckoAPI - API for CoinGecko to retrieve cryptocurrency stats

To install pyttsx3:
``` 
pip install pyttsx3
```

To install CoinGeckAPI:
``` 
pip install pycoingecko
```
Or find instructions to build from source [here](https://github.com/man-c/pycoingecko)

---

## Usage

Change into the project directory and run the program

```
cd goodMorning
python3 goodMorning.py
```

If you just want to run a talking clock and don't want to change the alarm time, comment or delete the lines (or copy/paste) in goodMorning.py's main() function so that it looks like this:

```{python}
def main():

    engine = pyttsx3.init()

    hour = current_time.hour
    if hour > 12:
        engine.say("Good Afternoon")

    else:
        engine.say("Good Morning")

    engine.say("It is ")
    engine.say(time_to_string())

    #TODO: Find some way for the user to select news sources
    engine.say(crypto_writer.crypto_stat_string(
            ['bitcoin', 'ethereum'], 'usd'))
    engine.runAndWait()
    engine.stop()

```