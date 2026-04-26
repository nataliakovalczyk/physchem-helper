"""Unit-aware physical chemistry helpers for physicists."""

from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

from .solutions import amount_from_molarity, dilution_volume, molarity
from .spectroscopy import photon_energy, photon_energy_per_mole
from .thermo import ideal_gas_pressure, ideal_gas_volume

try:
    from ._version import __version__
except ImportError:
    __version__ = "0+unknown"

__all__ = [
    "ureg",
    "Q_",
    "molarity",
    "amount_from_molarity",
    "dilution_volume",
    "ideal_gas_pressure",
    "ideal_gas_volume",
    "photon_energy",
    "photon_energy_per_mole",
]