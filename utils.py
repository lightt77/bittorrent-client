# bencode module: https://pypi.org/project/bencode.py/

import bencodepy

bencode = None

def read_torrent_file(file_path):
    global bencode
    if bencode == None:
        bencode = bencodepy.Bencode(encoding=None, encoding_fallback=None, dict_ordered=False, dict_ordered_sort=False)
    return bencode.read(file_path)