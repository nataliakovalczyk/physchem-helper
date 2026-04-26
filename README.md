# physchem-helper
Test assignment (lecture material) from RSE in Python course

[![tests](https://github.com/nataliakovalczyk/physchem-helper/actions/workflows/tests.yml/badge.svg?branch=work-branch)](https://github.com/nataliakovalczyk/physchem-helper/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/nataliakovalczyk/physchem-helper/branch/work-branch/graph/badge.svg)](https://codecov.io/gh/nataliakovalczyk/physchem-helper)
[![docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://nataliakovalczyk.github.io/physchem-helper/)

## Usage

```python
from physchem_helper import Q_, ideal_gas_pressure, molarity, photon_energy_per_mole

pressure = ideal_gas_pressure(Q_(1.0, "mol"), Q_(300, "K"), Q_(1.0, "L"))
print(pressure.to("atm"))

concentration = molarity(Q_(0.5, "mol"), Q_(250, "mL"))
print(concentration)

energy = photon_energy_per_mole(Q_(500, "nm"))
print(energy)