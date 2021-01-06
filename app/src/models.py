import attr

import numpy as np


@attr.s
class Observation:
    BTC: float = attr.ib()
    BCH: float = attr.ib()
    ETH: float = attr.ib()
    LTC: float = attr.ib()
    XRP: float = attr.ib()
    EOS: float = attr.ib()
    XLM: float = attr.ib()
    dBTC: float = attr.ib()
    dBCH: float = attr.ib()
    dETH: float = attr.ib()
    dLTC: float = attr.ib()
    dXRP: float = attr.ib()
    dEOS: float = attr.ib()
    dXLM: float = attr.ib()

    def as_tensor(self):
        return np.array([[self.BTC,
                        self.BCH,
                        self.ETH,
                        self.LTC,
                        self.XRP,
                        self.EOS,
                        self.XLM,
                        self.dBTC,
                        self.dBCH,
                        self.dETH,
                        self.dLTC,
                        self.dXRP,
                        self.dEOS,
                        self.dXLM,]])
