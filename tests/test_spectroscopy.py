import pytest

from physchem_helper import Q_, photon_energy, photon_energy_per_mole


def test_photon_energy():
    energy = photon_energy(Q_(500, "nm"))

    assert energy.to("J").magnitude == pytest.approx(3.97e-19, rel=1e-2)


def test_photon_energy_per_mole():
    energy = photon_energy_per_mole(Q_(500, "nm"))

    assert energy.to("kJ/mol").magnitude == pytest.approx(239, rel=1e-2)