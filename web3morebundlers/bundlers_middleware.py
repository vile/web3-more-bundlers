from typing import Any, Callable, Final

from web3 import Web3
from web3.middleware import Middleware
from web3.types import RPCEndpoint, RPCResponse

from .bundlers_provider import BundlersProvider

BUNDLERS_METHODS: Final[list[str]] = [
    "eth_sendBundle",
]


def construct_bundlers_middleware(bundlers_provider: BundlersProvider) -> Middleware:
    def bundlers_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], w3: Web3
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method not in BUNDLERS_METHODS:
                return make_request(method, params)
            else:
                resp = None
                resp = bundlers_provider.make_request(method, params)
                return {"result": [resp]}

        return middleware

    return bundlers_middleware
