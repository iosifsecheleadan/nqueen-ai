from project.ctrl.Controller import Controller
from project.domain.problem.nQueenProblem import NQueenProblem
from project.domain.state.permutation import Permutation


class ConsoleUI:
    def __init__(self, controller: Controller):
        self.controller = controller
        self.commands = {}
        self.addCommands()

    def mainMenu(self):
        self.printCommands()
        while True:
            userInput = input()
            try:
                self.commands[int(userInput)]()
            except ValueError:
                try:
                    self.commands[userInput]()
                except KeyError:
                    print("Wrong Input. Try again.")

    def nQueenDFS(self):
        boardSize = int(input("Please give board size: "))
        self.controller.setProblem(NQueenProblem())
        solution = self.controller.depthFirstSearch(Permutation(boardSize))
        print("Solution : " + str(solution))

    def nQueenGreedy(self):
        boardSize = int(input("Please give board size: "))
        self.controller.setProblem(NQueenProblem())
        solution = self.controller.greedy(Permutation(boardSize))
        print("Solution : " + str(solution))

    def printCommands(self):
        print("Commands : \n"
              "1 : nQueen dfs - deeply tries to find a solution to the problem\n"
              "2 : nQueen greedy - greedily tries to find a solution to the problem\n"
              "3 : help - display this screen\n"
              "4 : exit - exit the application\n")

    def addCommands(self):
        self.commands = {
            "nQueen dfs": self.nQueenDFS,
            1: self.nQueenDFS,
            "nQueen greedy": self.nQueenGreedy,
            2: self.nQueenGreedy,
            "help": self.printCommands,
            3: self.printCommands,
            "exit": quit,
            4: quit
        }
