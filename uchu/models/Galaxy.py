
class Galaxy:
    """
    Contains all the necessary parameters for a galaxy. 
    """
    def __init__(self, **kwargs):
        self.hlr = kwargs["hlr"]
        self.I_e = kwargs["I_e"]
        self.n = kwargs["n"]
        self.r_b = kwargs["r_b"]
        self.I_b = kwargs["I_b"]
        self.ipls = kwargs["ipls"]
        self.opls = kwargs["opls"]
        self.alpha = kwargs["alpha"]

    def get_params(self):
        return {"hlr": self.hlr, "I_e": self.I_e, "n": self.n, "r_b": self.r_b, "I_b": self.I_b, "ipls": self.ipls,
                "opls": self.opls, "alpha": self.alpha}

