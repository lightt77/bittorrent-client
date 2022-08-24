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
# - UDP tracker protocol specs: https://www.bittorrent.org/beps/bep_0015.html
# UDP tracker protocol specs: http://xbtt.sourceforge.net/udp_tracker_protocol.html
# - bencode module: https://pypi.org/project/bencode.py/
# - Python hex-to-bin transformations: https://stackoverflow.com/questions/1425493/convert-hex-to-binary

from constants import UTF_8
from tracker import tracker_announce, tracker_connect
from utils import read_torrent_file

# sample torrent(from https://webtorrent.io/free-torrents)
TORRENT_FILE_PATH = "./big-buck-bunny.torrent" 

def main():
    # read torrent file for tracker info
    torrent_file_dict = read_torrent_file(TORRENT_FILE_PATH)
    tracker_url = torrent_file_dict[b'announce'].decode(UTF_8) 
    print(f"Tracker url from torrent file: {tracker_url}")

    # connect to tracker
    tracker_connect(tracker_url)
    tracker_announce(tracker_url)

if __name__ == "__main__":
    main()