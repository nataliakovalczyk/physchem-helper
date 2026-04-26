import pytest

from physchem_helper import Q_, amount_from_molarity, dilution_volume, molarity


def test_molarity():
    concentration = molarity(Q_(0.5, "mol"), Q_(250, "mL"))

    assert concentration.to("mol/L").magnitude == pytest.approx(2.0)


def test_amount_from_molarity():
    amount = amount_from_molarity(Q_(2.0, "mol/L"), Q_(250, "mL"))

    assert amount.to("mol").magnitude == pytest.approx(0.5)


def test_dilution_volume():
    volume = dilution_volume(Q_(1.0, "mol/L"), Q_(0.1, "mol/L"), Q_(100, "mL"))

    assert volume.to("mL").magnitude == pytest.approx(10.0)