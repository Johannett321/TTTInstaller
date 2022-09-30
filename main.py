import urllib.request as urlreq
import time
import os
os.system('pip install progressbar')
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


print("Downloading Tic Tac Toe...")
time.sleep(0.5)

workdir = "CodeTicTacToe"
package_file_path = workdir + "/package.zip"

if os.path.isdir(workdir):
    print("Seems like you've already installed TicTacToe. Please delete the TicTacToe folder to reinstall")
    wait_for_keypress()
else:
    os.mkdir(workdir)
    file = urlreq.urlretrieve("https://github.com/Johannett321/CodeTicTacToe/releases/download/v1.0.0/1.0.0.zip",
                              package_file_path, show_progress)

    # Unpack
    print("Unpacking...")
    with zipfile.ZipFile(package_file_path, 'r') as zip_ref:
        zip_ref.extractall(workdir)

    os.remove(package_file_path)

    print("Done!")
    wait_for_keypress()
    os.chdir(workdir)
    os.system('pip install -r requirements.txt')
    os.system('python3 ' + "main.py")