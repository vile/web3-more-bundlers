# Web3 More Bundlers

This library works by injecting flashbots (`bundler`) as a new module in the Web3.py instance, which allows submitting "bundles" of transactions directly to miners. This is done by also creating a middleware which captures calls to `eth_sendBundle` and `eth_callBundle`, and sends them to an RPC endpoint which you have specified, which corresponds to `mev-geth`.

To apply correct headers we use the `flashbot` method which injects the correct header on `POST`.

> This is a superset project of [Flashbot's package](https://github.com/flashbots/web3-flashbots) for [Web3.py](https://github.com/ethereum/web3.py), and originally adapted from TitanBuilder's PR ([flashbots/web3-flashbots#76](https://github.com/flashbots/web3-flashbots/pull/76)). Flashbots currently only supports Web3.py version ^5.22.0 (not >=6).

## Quick Start

### Installing

Currently, this is not a published packaged, and is easiest to install using [Poetry](https://python-poetry.org/docs/) ([pipx](https://github.com/pypa/pipx)).
But, any package/env management solution that can install from Git/Github will work.

```bash
poetry add git+https://github.com/vile/web3-more-bundlers
```

### Example

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

## Migrating

Switching from the base Flashbots package to web3morebundlers is simple. This package initializes `flashbot` under the hood and exposes all existing `w3.flashbot` functions; only the initializer function needs to be changed (with an additional param).

Let's migrate flashbot's quickstart example:
```diff
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider
- from flashbots import flashbot
+ from web3morebundlers import bundler
from eth_account.account import Account
import os

ETH_ACCOUNT_SIGNATURE: LocalAccount = Account.from_key(os.environ.get("ETH_SIGNER_KEY"))
+ BUNDLER_ENDPOINTS = ["https://relay.flashbots.net", "https://rpc.titanbuilder.xyz", ...]

w3 = Web3(HTTPProvider("http://localhost:8545"))
- flashbot(w3, ETH_ACCOUNT_SIGNATURE)
+ bundler(w3=w3, signature_account=ETH_ACCOUNT_SIGNATURE, endpoint_uris=BUNDLER_ENDPOINTS)
```