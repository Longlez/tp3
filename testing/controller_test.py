from controllers.calcul_controller import CalculController
from logic.solving_equation import EquationSolver

controller = CalculController(EquationSolver())

def test_empty_input():
    assert "Erreur" in controller.compute("", "2", "3")

def test_non_numeric_input():
    assert "Erreur" in controller.compute("a", "2", "3")

def test_integration_valid():
    result = controller.compute("1", "-3", "2")
    assert "Δ" in result
    assert "x₁" in result

def test_integration_delta_negative():
    result = controller.compute("1", "0", "5")
    assert "Aucune racine" in result

def test_integration_a_zero():
    result = controller.compute("0", "2", "3")
    assert "Erreur" in result