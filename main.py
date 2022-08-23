# PREREQUISITES:
# "bencodepy" module should be installed on the machine. If it is not installed, install it using following pip command:
#   pip3 install bencodepy
#
# HOW TO RUN?
#   1. cd into directory of main.py
#   2. python3 main.py
# 
# USEFUL ARTICLES/DOCS:
# - bittorrent protocol specs: http://bittorrent.org/beps/bep_0003.html

from utils import read_torrent_file

# sample torrent(from https://webtorrent.io/free-torrents)
TORRENT_FILE_PATH = "./big-buck-bunny.torrent" 

def main():
    # read torrent file for tracker info
    torrent_file_dict = read_torrent_file(TORRENT_FILE_PATH)
    tracker_url = torrent_file_dict[b'announce'].decode("utf-8") 
    print(f"Tracker url from torrent file: {tracker_url}")

if __name__ == "__main__":
    main()