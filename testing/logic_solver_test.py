import pytest
from logic.solving_equation import EquationSolver

solver = EquationSolver()

def test_two_real_roots():
    delta, x1, x2 = solver.calculer(1, -3, 2)
    assert pytest.approx(delta) == 1
    assert pytest.approx(x1) == 2
    assert pytest.approx(x2) == 1


def test_one_real_root():
    delta, x1, x2 = solver.calculer(1, 2, 1)
    assert delta == 0
    assert x1 == x2 == -1


def test_negative_delta():
    result = solver.calculer(1, 0, 5)
    assert "Aucune racine réelle" in result


def test_a_cannot_be_zero():
    with pytest.raises(ValueError):
        solver.calculer(0, 2, 3)


def test_invalid_number():
    with pytest.raises(ValueError):
        solver.calculer(float("nan"), 2, 3)