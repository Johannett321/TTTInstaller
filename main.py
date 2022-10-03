import urllib.request as urlreq
import time
import os
os.system('pip3 install progressbar')
import zipfile

import progressbar as progressbar

pbar = None


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


def wait_for_keypress():
    print("[Press enter to open]", end="")
    input()
    print("Opening. Please wait...")


print("Downloading CodeTTT by Johan Svartdal...")
time.sleep(0.5)

workdir = "CodeTicTacToe"
package_file_path = workdir + "/package.zip"

if os.path.isdir(workdir):
    print("Seems like you've already installed TicTacToe. Please delete the TicTacToe folder to reinstall")
    wait_for_keypress()
else:
    os.mkdir(workdir)
    file = urlreq.urlretrieve("https://github.com/Johannett321/CodeTicTacToe/releases/download/v1.0.3/1.0.3.zip",
                              package_file_path, show_progress)

    # Unpack
    print("Unpacking...")
    with zipfile.ZipFile(package_file_path, 'r') as zip_ref:
        zip_ref.extractall(workdir)

    os.remove(package_file_path)

    os.chdir(workdir)
    os.system('pip3 install -r requirements.txt')
    print("Done!")
    wait_for_keypress()

    os.system('python3 ' + "Main.py")