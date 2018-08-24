import math


"""
=======================================
Surface Brightness Models
=======================================
"""

def sersic_intensity_profile(r, params):
    """
    A single-Sersic intensity profile. (Sersic, (1968))
    :param r: The radius being examined
    :param params: Parameters specified by the input galaxy.
    :return: 
    """
    hlr, I_e, n = params["hlr"], params["I_e"], params["n"]
    b_n = get_b(n)
    try:
        exponential = -b_n * (((r / hlr) ** (1 / n)) - 1)
        return I_e * math.exp(exponential)
    except:
        print("Input Error: Check your parameters.")
        return None


def sersic_sb_profile(r, params):
    """
    A Sersic surface brightness profile. (Sersic(1968), Graham(2005)) 
    :param r: 
    :param params: 
    :return: 
    """
    sb_eff, n, hlr = params["sb_eff"], params["n"], params["hlr"]

    try:
        piece_1 = 2.5 * get_b(n) / math.log(10)
        piece_2 = ((r / hlr) ** (1 / n)) - 1
        return (sb_eff + piece_1 * piece_2)
    except:
        print("Input Error: Check your parameters.")
        return None


def nuker_profile(r, params):
    """
    A galaxy profile defined by the Nuker Law (Erwin et al. (2003)).
    This profile is used as a means to probe details about a galaxy's core. It does not accurately plot a galaxy's
    light profile past the Half Light Radius
    :param r: The radius being examined
    :param params: Parameters for a galaxy
    :return: 
    """
    r_b, I_b, ipls, opls, alpha = params["r_b"], params["I_b"], params["ipls"], params["opls"], params["alpha"]
    if r == 0:
        return params["I_0"]

    p_1 = (opls - ipls) / alpha
    p_2 = (ipls - opls) / alpha
    f_1 = (r / r_b) ** (-ipls)
    f_2 = (1 + ((r / r_b) ** alpha))
    return I_b * (2 ** p_1) * f_1 * (f_2 ** p_2)

    # except:
    #     print("Input Error: Check your parameters.")
    #     return None


def core_sersic_profile(r, params):
    """
    A combined Nuker-law, Sersic model for intensity.
    :param r: The radius being examined
    :param params Parameters specified by the input galaxy
    :return: 
    """
    if r == 0:
        return params["I_0"]
    r_b, I_b, ipls, alpha = params["r_b"], params["I_b"], params["ipls"], params["alpha"]
    hlr, n = params["hlr"], params["n"]

    b_n = get_b(n)
    I_prime = I_b * (2 ** (-ipls / alpha)) * math.exp(b_n * (2 ** (1 / (alpha * n))) * ((r_b / hlr) ** (1 / n)))
    f_1 = 1 + (((r_b / r) ** alpha) ** (ipls / alpha))
    f_2 = math.exp(-b_n * ((r ** alpha + r_b ** alpha) / (hlr ** alpha)) ** (1/(n * alpha)))

    return I_prime * f_1 * f_2


def get_b(n):
    if n < 8:
        return (1.9992 * n) - 0.3271
    else:
        return (2 * n) - (1 / 3)
