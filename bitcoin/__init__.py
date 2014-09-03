# Distributed under the MIT/X11 software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

class MainParams(bitcoin.core.CoreChainParams):
    MESSAGE_START = b'\xaf\x45\x76\xee'
    DEFAULT_PORT = 10888
    RPC_PORT = 10889
<<<<<<< HEAD
    DNS_SEEDS = (('seed2.myriadcoin.org', 'seed1.myriadcoin.org'))

    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':9,
                       'SECRET_KEY' :178}
=======
    DNS_SEEDS = (("seed1.myriadcoin.org", "seed1.myriadcoin.org"),
		 ("seed2.myriadcoin.org", "seed2.myriadcoin.org"),
		 ("seed3.myriadcoin.org", "seed3.myriadcoin.org"),
		 ("seed4.myriadcoin.org", "seed4.myriadcoin.org"))
    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':9,
                       'SECRET_KEY' :128}
>>>>>>> 1b0374010e6e69af8a5d651efccaa4edd9a09713

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\xaf\x45\x76\xee'
    DEFAULT_PORT = 10888
    RPC_PORT = 10889
    DNS_SEEDS = (("seed1.myriadcoin.org", "seed1.myriadcoin.org"),
                 ("seed2.myriadcoin.org", "seed2.myriadcoin.org"),
                 ("seed3.myriadcoin.org", "seed3.myriadcoin.org"),
                 ("seed4.myriadcoin.org", "seed4.myriadcoin.org"))
    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':9,
                       'SECRET_KEY' :128}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xaf\x45\x76\xee'
    DEFAULT_PORT = 10888
    RPC_PORT = 10889
    DNS_SEEDS = (("seed1.myriadcoin.org", "seed1.myriadcoin.org"),
                 ("seed2.myriadcoin.org", "seed2.myriadcoin.org"),
                 ("seed3.myriadcoin.org", "seed3.myriadcoin.org"),
                 ("seed4.myriadcoin.org", "seed4.myriadcoin.org"))
    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':9,
                       'SECRET_KEY' :128}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = MainParams()
    else:
        raise ValueError('Unknown chain %r' % name)
