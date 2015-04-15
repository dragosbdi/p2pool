import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 8877
ADDRESS_VERSION = 12
RPC_PORT = 8878
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcreditaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: (50*100000000 >> (height + 1)//21000) if ((height + 1) < 30000) else (50*100000000 >> (height + 1)//210000)
POW_FUNC = data.hash256momentum
BLOCK_PERIOD = 60 # s
SYMBOL = 'BCR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcredit') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcredit/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcredit'), 'bitcredit.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/bcr/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/bcr/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/bcr/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**7//1000000000 - 1, 2**256//2**7 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
