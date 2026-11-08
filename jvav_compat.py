"""Small compatibility fixes around the pinned Jvav 3.x API."""

import jvav


class JavBusUtil(jvav.JavBusUtil):
    """Apply the bus_auth cookie supported by the Jvav constructor.

    Jvav 3.0.0 stores bus_auth but leaves its Cookie header commented out
    in get_headers. This adapter makes the documented option effective
    without modifying the third-party package.
    """

    def get_headers(self):
        headers = super().get_headers()
        if self.bus_auth:
            headers["Cookie"] = f"bus_auth={self.bus_auth};"
        return headers
