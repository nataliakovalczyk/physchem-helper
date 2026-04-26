"""Helpers connecting spectroscopy, quantum physics, and chemistry."""

from . import ureg

h = 6.62607015e-34 * ureg.joule * ureg.second
c = 299_792_458 * ureg.meter / ureg.second
N_A = 6.02214076e23 / ureg.mole


def photon_energy(wavelength):
    """Calculate the energy of one photon from wavelength.

    Uses ``E = h c / lambda``.

    Parameters
    ----------
    wavelength
        Photon wavelength.

    Returns
    -------
    pint.Quantity
        Energy of one photon converted to ``J``.
    """
    return (h * c / wavelength).to("J")


def photon_energy_per_mole(wavelength):
    """Calculate photon energy per mole of photons.

    Parameters
    ----------
    wavelength
        Photon wavelength.

    Returns
    -------
    pint.Quantity
        Energy per mole converted to ``kJ / mol``.
    """
    return (photon_energy(wavelength) * N_A).to("kJ / mol")