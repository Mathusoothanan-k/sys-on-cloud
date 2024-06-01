import psutil
import subprocess
import time
import os

def get_terminal_pid():
    # Get the PID of the current terminal session
    terminal_pid = os.getpid()
    return terminal_pid

def screen_short(pid):
    # Use psutil to get information about the process
    process = psutil.Process(pid)
    # Get the command line used to start the process
    cmdline = process.cmdline()
    print(f"Terminal PID: {pid}")
    print(f"Command Line: {' '.join(cmdline)}")
    
    # Take a screenshot of the terminal
    screenshot_filename = f"terminal_screenshot.png"
    subprocess.run(["scrot", "-u", screenshot_filename])
    print(f"Screenshot saved as {screenshot_filename}")

if __name__ == "__main__":
    terminal_pid = get_terminal_pid()
     # Start Ngrok service
    os.system('ngrok tcp 22 &')

    # Give Ngrok some time to start
    time.sleep(10)
    screen_short(terminal_pid)
