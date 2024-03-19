# Web3 More Bundlers

This library works by injecting flashbots (`bundler`) as a new module in the Web3.py instance, which allows submitting "bundles" of transactions directly to miners. This is done by also creating a middleware which captures calls to `eth_sendBundle` and `eth_callBundle`, and sends them to an RPC endpoint which you have specified, which corresponds to `mev-geth`.

To apply correct headers we use the `flashbot` method which injects the correct header on `POST`.

> This is a superset project of [Flashbot's package](https://github.com/flashbots/web3-flashbots) for [Web3.py](https://github.com/ethereum/web3.py), and originally adapted from TitanBuilder's PR (flashbots/web3-flashbots#76). Flashbots currently only supports Web3.py version ^5.22.0 (not >=6).

## Quick Start

```python
import os

from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from web3 import HTTPProvider, Web3

from web3morebundlers import bundler

ETH_ACCOUNT_SIGNATURE: LocalAccount = Account.from_key(os.environ.get("ETH_SIGNER_KEY"))
BUNDLER_ENDPOINTS = ["https://relay.flashbots.net", "https://rpc.titanbuilder.xyz", ...]


w3 = Web3(HTTPProvider("http://localhost:8545"))
bundler(w3=w3, signature_account=ETH_ACCOUNT_SIGNATURE, endpoint_uris=BUNDLER_ENDPOINTS)
```

Now the `w3.flashbots.sendBundle` method should be available to you. Look in [examples/simple.py](./examples/simple.py) for usage examples.

## Using Testnets

Currently, the base flashbots package only supports Goerli. To use Goerli, add the Goerli **relay** RPC to the `bundler` function arguments.

```python
bundler(w3=w3, signature_account=ETH_ACCOUNT_SIGNATURE, endpoint_uris=BUNDLER_ENDPOINTS, flashbots_uri="https://relay-goerli.flashbots.net")
```
