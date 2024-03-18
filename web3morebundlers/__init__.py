from eth_account.signers.local import LocalAccount
from flashbots import Flashbots
from web3 import Web3
from web3._utils.module import attach_modules

from .bundlers_middleware import construct_bundlers_middleware
from .bundlers_provider import BundlersProvider


def bundler(w3: Web3, signature_account: LocalAccount, endpoint_uris: list) -> None:
    providers = BundlersProvider(signature_account, endpoint_uris)
    bundlers_middleware = construct_bundlers_middleware(providers)
    w3.middleware_onion.add(bundlers_middleware)

    # attach modules to add the new namespace commands
    attach_modules(w3, {"flashbots": (Flashbots,)})