from project.domain.problem.problem import Problem
from project.domain.state.permutation import Permutation


class NQueenProblem(Problem):
    def __init__(self):
        pass

    def validity(self, permutation: Permutation):
        """
        Return number of elements placed diagonally
            respective to each other
        :return: integer
        """
        val = 0
        for i in range(0, permutation.size):
            for j in range(i + 1, permutation.size):
                if permutation.getElements()[i] == 0:
                    return val
                elif permutation.getElements()[j] == 0:
                    val += 1
                elif (permutation.getElements()[i] == permutation.getElements()[j] + (j - i)) or \
                        (permutation.getElements()[i] == permutation.getElements()[j] - (j - i)) or \
                        (permutation.getElements()[i] == permutation.elements[j]):
                    # if on main diagonal or on secondary diagonal or on same column
                    val += 1
        return val

    def getSortedChildren(self, permutation: Permutation):
        children = self.__expandInformed(permutation)
        children.sort(key=lambda child: self.validity(child))
        return children

    def __expandInformed(self, permutation: Permutation):
        """
        Returns the list of child nodes
        :return: list <Permutations>
        """
        children = []
        index = permutation._find0()
        for change in range(1, permutation.size + 1):
            if change not in permutation.getElements():
                child = Permutation(permutation.size)
                elements = permutation.getElements()
                elements[index] = change
                child.setElements(elements)
                children.append(child)
        return children

    def __str__(self):
        string = "NQueenPermutation :"
        for elem in self.elements:
            string += " " + str(elem)
        string += " - " + str(self.validity())
        return string
