from logic.solving_equation import EquationSolver
from datetime import datetime
import os

class CalculController:

    def __init__(self, solver: EquationSolver):
        self.solver = solver
        self.log_file = "log.txt"

        # Crée le fichier s'il n'existe pas encore
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write("=== Historique des calculs ===\n")

    def compute(self, a_text: str, b_text: str, c_text: str) -> str:
        # Vérifier si les champs sont vides
        if not a_text or not b_text or not c_text:
            return "Erreur : Veuillez remplir tous les champs."

        # Conversion en nombre
        try:
            value_a = float(a_text)
            value_b = float(b_text)
            value_c = float(c_text)
        except ValueError:
            return "Erreur : Les valeurs doivent être des nombres."

        # Calcul
        try:
            result = self.solver.calculer(value_a, value_b, value_c)

            if isinstance(result, tuple):
                delta, x1, x2 = result
                text = f"Δ = {delta:.2f}\nx₁ = {x1:.2f}\nx₂ = {x2:.2f}"
            else:
                text = result  

            # Logging dans le fichier
            self._log(value_a, value_b, value_a, error_message)
            return text

        except ValueError as e:
            error_message = f"Erreur : {e}"
            self._log(value_a, value_b, value_a, error_message)
            return error_message

        except Exception as e:
            error_message = "Erreur inattendue."
            self._log(value_a, value_b, value_a, error_message)
            return error_message

    def _log(self, value_a, value_b, value_c, result):
        """Écrit l'historique dans log.txt"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"a={value_a}, b={value_b}, c={value_c} → {result}\n"
            )