import pytest

from physchem_helper import Q_, ideal_gas_pressure, ideal_gas_volume


def test_ideal_gas_pressure():
    pressure = ideal_gas_pressure(Q_(1.0, "mol"), Q_(300, "K"), Q_(1.0, "L"))

    assert pressure.to("atm").magnitude == pytest.approx(24.6, rel=1e-2)


def test_ideal_gas_volume():
    volume = ideal_gas_volume(Q_(1.0, "mol"), Q_(300, "K"), Q_(1.0, "atm"))

    assert volume.to("L").magnitude == pytest.approx(24.6, rel=1e-2)