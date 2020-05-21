"""
Authentication for Environmental variables
"""

import os
import sys


def auth_env():
    """
    returns endpoint and subscription key
    """

    if "COGNITIVE_SERVICE_KEY" in os.environ:
        subscription_key = os.environ["COGNITIVE_SERVICE_KEY"]
    else:
        sys.exit('No key present, please load key unto os environment and retry')

    if "COGNITIVE_ENDPOINT" in os.environ:
        endpoint = os.environ["COGNITIVE_ENDPOINT"]
    else:
        sys.exit('No key present, please load endpoint unto os environment and retry')

    return endpoint, subscription_key
