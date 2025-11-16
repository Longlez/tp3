import math
from typing import Tuple, Union

class EquationSolver:
    """ Constructeur de la class"""
    def __init__(self):
        pass

    """ Methode qui fait la resolution de l'equation """
    def calculer(self, value_a: float, value_b: float, value_c: float) -> Union[str, Tuple[float, float, float]]:
        """Retourne (delta, x1, x2) ou un message d'erreur"""
        if value_a == 0:
            raise ValueError("Le coefficient 'a' ne peut pas être 0")

        delta = value_b**2 - 4*value_a*value_c

        if delta < 0:
            return f"Pas de racines réelles (Δ = {delta:.2f})."

        elif delta == 0:
            x = -value_b/ (2 * value_a)
            return (delta, x, x)

        else:
            racine_delta = math.sqrt(delta)
            value_x1 = (-value_b + racine_delta) / (2 * value_a)
            value_x2 = (-value_b - racine_delta) / (2 * value_a)
            return (delta, value_x1, value_x2)