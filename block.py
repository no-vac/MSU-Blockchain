import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    #timestamp = datetime.datetime.now()


    def __init__(self, data):
        self.data = data


    def hash(self):
        timestamp = datetime.datetime.now()

        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        # ties all blocks together, changing hash of any block
        # changes all hashes of block that come after it
        str(self.previous_hash).encode('utf-8') +

        #str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        print(timestamp)
        print(self.blockNo)
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: "+ str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce)+ "\nPrevious Hash: " + str(self.previous_hash)+ "\n-------------------------------------------------------------------------"
#     + "\nTimestamp: " + str(self.timestamp)
