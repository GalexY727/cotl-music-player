from pyautogui import *
import pyautogui, keyboard, json, time
from stopwatch import Stopwatch
from ahk import AHK
from pick import pick
from os import listdir

ahk = AHK()
#Notes to keybinds!!!
note_to_key = {
    '1Key0': 'y',
    '1Key1': 'u',
    '1Key2': 'i',
    '1Key3': 'o',
    '1Key4': 'p',
    '1Key5': 'h',

    '1Key6': 'j',
    '1Key7': 'k',
    '1Key8': 'l',
    '1Key9': ';',
    '1Key10': 'n',

    '1Key11': 'm',
    '1Key12': ',',
    '1Key13': '.',
    '1Key14': '/'
}

stopwatch = Stopwatch(2)
def main():
    print('Starting \ueb44')
    # TODO: Prompt user for song name and determine the json from that
    while 1:
        loop(prompt_song())

def prompt_song():
    options_for_code = [item.replace('.json', '') for item in listdir('songs//')]
    options_for_code = [options_for_code.pop(options_for_code.index('interstellar'))] + options_for_code
    
    option, index = pick([item.replace("_", " ").title() for item in options_for_code], 'Song choice selector', indicator='\udb83\udf74', default_index=0)
    print(f'You picked {option}')
    song = ''
    with open(f'songs/{options_for_code[index]}.json') as json_file:
        song = json.load(json_file)
    print('Song Loaded!')
    print('Song length: ' + str(int(song[0]['songNotes'][-1]['time']/1000/60)) + ' minutes ' + str(int(song[0]['songNotes'][-1]['time']/1000%60)) + ' seconds')
    return song

def loop(song):
    # wait for the user to press '\'
    keyboard.wait('\\')
    stopwatch.stop()
    stopwatch.reset()
    stopwatch.start()
    
    # get the last index in the json to find the song duration
    song_length = song[0]['songNotes'][-1]['time'] # integer (ms)

    last_note_played_timestamp = 0
    # 86.5
    while stopwatch.duration < song_length/1000:
        current_duration = stopwatch.duration
        if keyboard.is_pressed('ctrl+backspace'):
            exit()
        if keyboard.is_pressed('backspace'):
            break
        if keyboard.is_pressed('-'):
            print('\nPaused current timestamp: ' + str(last_note_played_timestamp) + '\nPress = to resume\n')
            stopwatch.stop()
            keyboard.wait('=')
            print('Resumed\n')
            stopwatch.start()            
        printProgressBar(current_duration, song_length/1000, prefix = '', suffix = '', length = 20)
        # use stopwatch as a timer to play notes
        # get the first item in json that has a 'time' key
        # if time has passed then delete that item and check again
        keysToPress = []
        while len(song[0]['songNotes']) > 0 and song[0]['songNotes'][0]['time']/1000 <= current_duration:
            # check if there is a key that contains the json property '1Key'
            if '1Key' not in song[0]['songNotes'][0]['key']:
                # turn '2Key' into '1Key'
                song[0]['songNotes'][0]['key'] = '1' + song[0]['songNotes'][0]['key'][1:]
            if (current_duration - song[0]['songNotes'][0]['time']/1000) < 0.1:
                keysToPress.append(note_to_key[song[0]['songNotes'][0]['key']])
                last_note_played_timestamp = song[0]['songNotes'][0]['time']
            del song[0]['songNotes'][0]
        
        if keysToPress == []:
            continue
        
        for key in keysToPress:
            ahk.key_down(key)

        time.sleep(0.03)

        for key in keysToPress:
            ahk.key_up(key)
    
    print('Song Complete!!')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = '\r'):
    '''
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. '\r', '\r\n') (Str)
    '''
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == '__main__':
    main()