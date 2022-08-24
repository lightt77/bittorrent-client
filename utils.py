# bencode module: https://pypi.org/project/bencode.py/

import random
import bencodepy

bencode = None

def read_torrent_file(file_path):
    global bencode
    if bencode == None:
        bencode = bencodepy.Bencode(encoding=None, encoding_fallback=None, dict_ordered=False, dict_ordered_sort=False)
    return bencode.read(file_path)

def get_bytes(bits, buffer_size):
    bytes = 0
    for bit in bits:
        bytes = (bytes << 1)
        if bit == '1':
            bytes |= 1
    return bytes.to_bytes(buffer_size, "big")

def parse_byte(bytes, byte_offset, required_bit_size):
    result = 0
    bits_consumed = 0
    for index, byte in enumerate(bytes):
        if index >= byte_offset and bits_consumed < required_bit_size:
            result = (result << 8) | byte 
            bits_consumed += 8
    return f"{result:0>{required_bit_size}b}"

def generate_transaction_id():
    return f"{random.randint(1, 1000):0>32b}"