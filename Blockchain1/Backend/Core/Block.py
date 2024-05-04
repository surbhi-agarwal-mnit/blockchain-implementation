class Block:
    """
    Block is a storage containter that stores transactions
    """

    def __init__(self, Height, Blocksize, BlockHeader, TxCount, Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.Txcount = TxCount
        self.Txs = Txs
        print("Block created, with hash: "+BlockHeader.blockHash)
        