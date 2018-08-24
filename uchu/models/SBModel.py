import math


"""
=======================================
Surface Brightness Models
=======================================
"""

# todo alter functions to take in galaxy parameters instead of setting them manually (much better, more eloquent soln)

def sersic_profile(r, hlr, I_e, n):
    """
    A single-Sersic profile. (Sersic, (1968))
    :param r: The radius being examined
    :param hlr: The half-light radius of the galaxy
    :param I_e: Intensity at the half-light radius
    :param n: The degree of curvature of the galaxy (Sersic index)
    :return: 
    """
    b_n = (2 * n) - (1 / 3)

    return I_e * math.exp(-b_n * (((r / hlr) ** (1/n)) - 1))


def nuker_profile(r, r_b, I_b, ipls, opls, alpha):
    """
    A galaxy profile defined by the Nuker Law (Erwin et al. (2003))
    :param r: The radius being examined
    :param r_b: The core radius.
    :param I_b: The intensity at the core radius.
    :param ipls: The Inner Power Law Slope (IPLS) -- gamma
    :param opls: The Outer Power Law Slope (OPLS) -- beta
    :param alpha: Transition between power laws
    :return: 
    """
    p_law_one = I_b * (2 ** ((opls - ipls) / alpha)) * ((r / r_b) ** -ipls)
    p_law_two = (1 + ((r / r_b) ** alpha)) ** ((ipls - opls) / alpha)
    return p_law_one * p_law_two


def nuker_sersic_profile(r, r_b, hlr, I_b, ipls, alpha, n):
    """
    A combined Nuker-law, Sersic model for surface brightness.
    :param r: The radius being examined
    :param r_b: Radius of the core
    :param hlr: The Half-Light radius of the galaxy
    :param I_b: Intensity at the core radius
    :param ipls: The Inner Power Law Slope (IPLS) -- gamma
    :param alpha: The sharpness of transition between inner and outer regimes.
    :param n: The degree of curvature (Sersic index)
    :return: 
    """
    b_n = (2 * n) - (1 / 3)
    I_prime = I_b * (2 ** (-ipls / alpha)) * math.exp(b_n * (2 ** (1/alpha) * (r_b / hlr)) ** (1 / n))
    nuker_comp = (1 + (r_b / r) ** alpha) ** (ipls / alpha)
    sersic_comp = math.exp(-b_n * ((r ** alpha + r_b ** alpha) / (hlr ** alpha)) ** (1 / (alpha * n)))

    return I_prime * nuker_comp * sersic_comp


