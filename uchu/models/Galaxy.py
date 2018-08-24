
class Galaxy:
    """
    Contains all the necessary parameters for a galaxy. 
    """
    def __init__(self, hlr=None, I_e=None, n=None, r_b=None, I_b=None, ipls=None, opls=None, alpha=None, sb_eff=None,
                 I_0=None):
        try:
            self.hlr = hlr
        except KeyError:
            self.hlr = None
        self.I_e = I_e
        self.n = n
        self.r_b = r_b
        self.I_b = I_b
        self.ipls = ipls
        self.opls = opls
        self.alpha = alpha
        self.sb_eff = sb_eff
        self.I_0 = I_0

    def get_params(self):
        return {"hlr": self.hlr, "I_e": self.I_e, "n": self.n, "r_b": self.r_b, "I_b": self.I_b, "ipls": self.ipls,
                "opls": self.opls, "alpha": self.alpha, "sb_eff": self.sb_eff, "I_0": self.I_0}

