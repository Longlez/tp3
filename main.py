from PyQt5.QtWidgets import QApplication, QWidget
from controllers.calcul_controller import CalculController
from ui.gui import SolverUI
from logic.solving_equation import EquationSolver
import sys

def main():
    print("Calculette 2nd Degree")
    application = QApplication(sys.argv)
    solver = EquationSolver()
    controller = CalculController(solver)
    interface = SolverUI(controller)
    interface.show()
    sys.exit(application.exec_())

""" Lance notre programme """
if __name__ == "__main__":
    main()