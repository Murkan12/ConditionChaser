import subprocess
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, cwd, commands):
        self.cwd = cwd
        self.commands = commands

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File {event.src_path} has been modified. Running command...")
            self.run_command()
    
    def run_command(self):
        commands = self.commands
        for command in commands:
            subprocess.run(command, shell=True, cwd=self.cwd)
