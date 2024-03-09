import threading
import os

def folder(folder_path):
    """
    Create a folder if it does not exist.

    Parameters:
        folder_path (str): The path of the folder to create.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def file(file_path, content=""):
    """
    Create a file if it does not exist.

    Parameters:
        file_path (str): The path of the file to create.
        content (str): Optional. Content to write to the file.
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' created successfully.")
    else:
        print(f"File '{file_path}' already exists.")

folder("python-tor-proxy")

if os.path.exists("python-tor-proxy/torrc"):
            socksPort = int(3000)
            file("python-tor-proxy/torrc", "SocksPort " + str(socksPort) + "\nHiddenServiceDir python-tor-proxy/HiddenServiceDir")

def tor():
  os.system("tor -f python-tor-proxy/torrc")

def hide_output():
    # Redirect stdout and stderr to /dev/null
    os.dup2(os.open(os.devnull, os.O_WRONLY), 1)
    os.dup2(os.open(os.devnull, os.O_WRONLY), 2)

def run_tor():
  torThread = threading.Thread(target=tor)
  torThread.daemon = True
  torThread.run = hide_output
  torThread.start()
  return torThread

folder("python-tor-proxy/HiddenServiceDir")
run_tor()
