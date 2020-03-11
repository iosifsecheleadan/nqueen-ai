from project.ctrl.Controller import Controller
from project.domain.problem.problem import Problem


class ProblemController(Controller):
    def __init__(self, problem: Problem):
        self.problem = problem

    def setProblem(self, problem):
        self.problem = problem

    def depthFirstSearch(self, permutation):
        children = permutation.expand()
        while len(children):
            permutation = children.pop(0)
            if self.problem.validity(permutation) == 0: return permutation
            children = permutation.expand() + children

    def greedy(self, permutation):
        while True:
            if permutation.solution(): return permutation
            permutation = self.problem.getSortedChildren(permutation).pop(0)

