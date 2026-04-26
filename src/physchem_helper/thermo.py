"""Helpers for unit-aware thermodynamic calculations."""

from . import ureg

R = 8.31446261815324 * ureg.joule / (ureg.mole * ureg.kelvin)


def ideal_gas_pressure(amount, temperature, volume):
    """Calculate pressure from the ideal gas law.

    Uses ``P V = n R T``.

    Parameters
    ----------
    amount
        Amount of gas.
    temperature
        Gas temperature.
    volume
        Gas volume.

    Returns
    -------
    pint.Quantity
        Pressure converted to ``Pa``.
    """
    return (amount * R * temperature / volume).to("Pa")


def ideal_gas_volume(amount, temperature, pressure):
    """Calculate volume from the ideal gas law.

    Uses ``P V = n R T``.

    Parameters
    ----------
    amount
        Amount of gas.
    temperature
        Gas temperature.
    pressure
        Gas pressure.

    Returns
    -------
    pint.Quantity
        Volume converted to ``m^3``.
    """
    return (amount * R * temperature / pressure).to("m^3")