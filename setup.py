# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["web3morebundlers"]

package_data = {"": ["*"]}

install_requires = ["web3>=5.22.0,<6", "flashbots>=1.1.1,<2"]

setup_kwargs = {
    "name": "web3morebundlers",
    "version": "0.1.0",
    "description": "Superset of Flashbots' plugin for Web3.py allowing bundles to be submitted to many miners.",
    "long_description": 'This library works by injecting flashbots (`bundler`) as a new module in the Web3.py instance, which allows submitting "bundles" of transactions directly to miners. This is done by also creating a middleware which captures calls to `eth_sendBundle` and `eth_callBundle`, and sends them to an RPC endpoint which you have specified, which corresponds to `mev-geth`.',
    "long_description_content_type": "text/markdown",
    "author": "Vile",
    "author_email": "111662603+vile@users.noreply.github.com",
    "url": "https://github.com/vile/web3-more-bundlers",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
