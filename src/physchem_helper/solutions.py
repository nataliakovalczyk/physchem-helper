"""Helpers for unit-aware solution chemistry calculations."""


def molarity(amount, volume):
    """Calculate molar concentration from amount of substance and volume.

    Parameters
    ----------
    amount
        Amount of substance, e.g. ``0.5 mol``.
    volume
        Solution volume, e.g. ``250 mL``.

    Returns
    -------
    pint.Quantity
        Concentration converted to ``mol / L``.
    """
    return (amount / volume).to("mol / L")


def amount_from_molarity(concentration, volume):
    """Calculate amount of substance from concentration and volume.

    Parameters
    ----------
    concentration
        Molar concentration, e.g. ``0.1 mol / L``.
    volume
        Solution volume, e.g. ``250 mL``.

    Returns
    -------
    pint.Quantity
        Amount of substance converted to ``mol``.
    """
    return (concentration * volume).to("mol")


def dilution_volume(initial_concentration, final_concentration, final_volume):
    """Calculate stock-solution volume needed for a dilution.

    Uses the relation ``C1 * V1 = C2 * V2``.

    Parameters
    ----------
    initial_concentration
        Stock concentration.
    final_concentration
        Target concentration.
    final_volume
        Target final volume.

    Returns
    -------
    pint.Quantity
        Required stock-solution volume, expressed in the units of ``final_volume``.
    """
    volume = final_concentration * final_volume / initial_concentration
    return volume.to(final_volume.units)