from datetime import datetime

file_path = "/home/file_python.txt"

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(file_path, "a") as file:
    file.write("Script executed at: " + current_time + "\n")
