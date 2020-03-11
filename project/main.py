from project.ctrl.problemController import ProblemController
from project.domain.problem.nQueenProblem import NQueenProblem
from project.ui.console import ConsoleUI


class Main:
    def __init__(self):
        problem = NQueenProblem()
        self.controller = ProblemController(problem)
        self.console = ConsoleUI(self.controller)

    def run(self):
        self.console.mainMenu()


main = Main()
main.run()
