import socket
from utils import generate_transaction_id, get_bytes, parse_byte

client_socket = None
connection_id = None

TRACKER_ACTIONS = {
    "connect": f"{0x00:0>32b}",
    "announce": f"{0x01:0>32b}"
}

def tracker_connect(tracker_url):    
    global client_socket
    global connection_id
    try:
        if client_socket == None:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            url, port = tracker_url.split("://")[1].split(":")
            addr = (url, int(port))
            client_socket.connect(addr)
        
        msg = ""
        msg += f"{0x41727101980:0>64b}"                         # protocol_id, magic constant as per specs (https://www.bittorrent.org/beps/bep_0015.html)
        msg += TRACKER_ACTIONS["connect"]                       # 'connect' action
        transaction_id = generate_transaction_id()    
        msg += transaction_id                                   # randomly generated 32-bit transaction_id
        encoded_msg = get_bytes(msg, 16)

        print(f"[TRACKER CONNECT] Tracker connect called with message: {encoded_msg}")
        client_socket.send(encoded_msg)
        resp = client_socket.recv(128)
        print(f"[TRACKER CONNECT] Tracker connect resp: {resp}")

        if len(resp) != 16:
            raise RuntimeError(f"[TRACKER CONNECT] Response is not 16 bytes long. Resp: {resp}")
        
        received_transaction_id = parse_byte(resp, 4, 32)
        if transaction_id != received_transaction_id:
            raise RuntimeError(f"[TRACKER CONNECT] Response does not have expected transaction id.\n Received transaction id: {received_transaction_id},\n Expected transaction id: {transaction_id}")

        received_action = parse_byte(resp, 0, 32) 
        if received_action != TRACKER_ACTIONS["connect"]:
            raise RuntimeError(f"[TRACKER CONNECT] Response does not have expected action.\n Received action: {received_action},\n Expected action: {TRACKER_ACTIONS['connect']}")

        connection_id = parse_byte(resp, 8, 64)
        print(f"[TRACKER CONNECT] Received connection id for tracker connect: {connection_id}")

        return resp
    finally:
        print("Shutting down socket..")
        client_socket.shutdown(socket.SHUT_RDWR)

def tracker_announce(tracker_url):
    pass