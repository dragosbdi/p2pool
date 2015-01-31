from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcredit']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//30 # shares
REAL_CHAIN_LENGTH = 24*60*60//30 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'b1dc7ed1dc11e0d1'.decode('hex')
PREFIX = 'ba0c05e7ad100301'.decode('hex')
P2P_PORT = 8777
MIN_TARGET = 0
MAX_TARGET = 2**256//2**7 - 1
PERSIST = True
WORKER_PORT = 8776
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-bcr'
VERSION_CHECK = lambda v: 300700 <= v
VERSION_WARNING = lambda v: 'Upgrade Bitcredit to >=0.30.7!' if v < 300700 else None
