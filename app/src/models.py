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
    CryptoMajor: float = attr.ib()
    CryptoMajor_delta: float = attr.ib()

    def as_tensor(self):
        return np.array([[self.BTC,
                        self.BCH,
                        self.ETH,
                        self.LTC,
                        self.XRP,
                        self.EOS,
                        self.XLM,
                        self.CryptoMajor,
                        self.CryptoMajor_delta]])
