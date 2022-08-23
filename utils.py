# bencode module: https://pypi.org/project/bencode.py/

import bencodepy

bencode = None

def readTorrentFile(filePath):
    global bencode
    if bencode == None:
        bencode = bencodepy.Bencode(encoding=None, encoding_fallback=None, dict_ordered=False, dict_ordered_sort=False)
    return bencode.read(filePath)