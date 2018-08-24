import math


"""
=======================================
Surface Brightness Models
=======================================
"""

def sersic_profile(r, params):
    """
    A single-Sersic profile. (Sersic, (1968))
    :param r: The radius being examined
    :param params: Parameters specified by the input galaxy.
    :return: 
    """
    try:
        hlr, I_e, n = params["hlr"], params["I_e"], params["n"]
        b_n = (2 * n) - (1 / 3)

        return I_e * math.exp(-b_n * (((r / hlr) ** (1/n)) - 1))
    except:
        print("Input Error: Check your parameters.")
        return None

def nuker_profile(r, params):
    """
    A galaxy profile defined by the Nuker Law (Erwin et al. (2003))
    :param r: The radius being examined
    :param params: Parameters for a galaxy
    :return: 
    """
    r_b, I_b, ipls, opls, alpha = params["r_b"], params["I_b"], params["ipls"], params["opls"], params["alpha"]
    try:
        p_law_one = I_b * (2 ** ((opls - ipls) / alpha)) * ((r / r_b) ** -ipls)
        p_law_two = (1 + ((r / r_b) ** alpha)) ** ((ipls - opls) / alpha)
        return p_law_one * p_law_two
    except:
        print("Input Error: Check your parameters.")
        return None


def nuker_sersic_profile(r, params):
    """
    A combined Nuker-law, Sersic model for surface brightness.
    :param r: The radius being examined
    :param params Parameters specified by the input galaxy
    :return: 
    """
    try:
        r_b, I_b, ipls, alpha = params["r_b"], params["I_B"], params["ipls"], params["alpha"]
        hlr, n = params["hlr"], params["n"]
        b_n = (2 * n) - (1 / 3)
        I_prime = I_b * (2 ** (-ipls / alpha)) * math.exp(b_n * (2 ** (1/alpha) * (r_b / hlr)) ** (1 / n))
        nuker_comp = (1 + (r_b / r) ** alpha) ** (ipls / alpha)
        sersic_comp = math.exp(-b_n * ((r ** alpha + r_b ** alpha) / (hlr ** alpha)) ** (1 / (alpha * n)))

        return I_prime * nuker_comp * sersic_comp
    except:
        print("Input Error: Check your parameters.")
        return None


