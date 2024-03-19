from typing import Any, Optional

from eth_account.signers.local import LocalAccount
from flashbots import flashbot
from web3 import Web3

from .bundlers_middleware import construct_bundlers_middleware
from .bundlers_provider import BundlersProvider


def bundler(
    w3: Web3,
    signature_account: LocalAccount,
    endpoint_uris: list[str],
    flashbots_uri: Optional[Any] = None,
) -> None:
    """
    Injects the base flashbots module and middleware, as well as bundler middleware to w3.
    """

    _flashbots_uri = flashbots_uri or "https://relay.flashbots.net"
    flashbot(w3, signature_account, _flashbots_uri)
    providers = BundlersProvider(signature_account, endpoint_uris)
    bundlers_middleware = construct_bundlers_middleware(providers)
    w3.middleware_onion.add(bundlers_middleware)
