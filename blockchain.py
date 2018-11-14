from block import Block
import datetime
import hashlib

class Blockchain:
    #WHAT IS THIS
    #increasing difficulty nunmber decreases target range
    # so the acceptable range becomes smaller.
    # (block's hash) must be <= (target range) to be accepted
    diff = 3

    #maxNonce = 2**32
    #target = 2 ** (256-diff)

    maxNonce = 2**10
    target = 2 ** (256-diff)
    print(target)

    block = Block("head")
    # start of list 'head'. var = head = block, head does not point to same as block
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            # current block hash <= target
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else: block.nonce += 1

blockchain = Blockchain()
num_blocks = 5000

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next

# TODO: test how adding works, print out list of added blocks
#for i in range(num_blocks):
#    blockchain.add(Block("Block"))


for n in range(num_blocks):
    blockchain.mine(Block("Block" + str(n+1)))


#blockchain.mine(Block("Block" + str(1)))
#blockchain.mine(Block("Block" + str(2)))
#blockchain.mine(Block("Block" + str(3)))
#blockchain.mine(Block("Block" + str(4)))
