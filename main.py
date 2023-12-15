import sys
import time
from watchdog.observers import Observer
from utils.FileChangeHandler import FileChangeHandler

if __name__ == "__main__":
    path = sys.argv[1]
    cwd = sys.argv[2]
    commands = sys.argv[3:]
    event_handler = FileChangeHandler(cwd, commands)
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

