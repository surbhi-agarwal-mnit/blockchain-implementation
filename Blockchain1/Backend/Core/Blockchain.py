import sys
sys.path.append('/Users/surbh/Desktop/BITCOIN')
from Blockchain1.Backend.Core.Block import Block 
from Blockchain1.Backend.Core.Blockheader import *
from Blockchain1.Backend.Util1.Util import hash256
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Surbhi's Blockchain Sent{BlockHeight} Bitcoins to MNIT"
        merkleRoot = hash256(Transaction)
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader, 1, Transaction))
        # print(self.chain)

    def main(self):
        if len(self.chain) == 0 :
            self.GenesisBlock()
        count = 15
        while count >= 0:
            lastBlockHash = self.chain[len(self.chain)-1].BlockHeader.prevBlockHash
            blockHeight = self.chain[len(self.chain)-1].Height+1
            self.addBlock(blockHeight,lastBlockHash)
            count -= 1


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
    
