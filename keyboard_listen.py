import keyboard as kb
import time

# # Register an abbreviation that replaces 'hw' with 'hello, world'
# keyboard.add_abbreviation('hw', 'hello, world')

# # Keep the program running to detect keystrokes
# print("Abbreviation 'hw' registered. Type 'hw' followed by a space to see it in action.")

# # This will keep the program running


# while 1:
#     event=kb.read_event()  
#     print(event.name)
#     time.sleep(0.3)

key = 140

while 1:
    if kb.is_pressed(key):
        while kb.is_pressed(key):
            print("calc on")
            time.sleep(0.1)
    if kb.is_pressed('esc'):
        break
    if kb.is_pressed(key)==False:
        print("not calc")
        time.sleep(0.1)
time.sleep(0.05)



# def on_call():
#     print('calc on')
    
# kb.add_hotkey(key, on_call)

# kb.wait('esc')


# import keyboard

# print("Press the calculator key...")
# event = keyboard.read_event()
# print(f"Key name: {event.name}, Scan code: {event.scan_code}")