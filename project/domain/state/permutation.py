from copy import deepcopy
from numpy import random
from project.domain.error.statError import StatError
from project.domain.state.State import State


class Permutation(State):
    def __init__(self, number: int = 0):
        self.size = number
        self.elements = [0] * number

    def setElements(self, elements):
        self.elements = deepcopy(elements)

    def getElements(self):
        return deepcopy(self.elements)

    def solution(self):
        return self.elements.count(0) == 0

    def expand(self): #uninformed
        """
        Returns the list of child nodes
        :return: list<Permutations>
        """
        children = []
        index = self._find0()
        if index >= self.size: return children
        for change in range(1, self.size + 1):
            child = Permutation(self.size)
            elements = self.getElements()
            elements[index] = change
            child.setElements(elements)
            children.append(child)
        return children

    def ranomizeUniform(self):
        self.elements = []
        while len(self.elements) < self.size:
            current = self.__getRandomNumber(self.size)
            if current not in self.elements:
                self.elements.append(current)

    def mutate(self, probability=10):
        if probability > 100 or 0 > probability:
            raise StatError("Mutation of probability " + str(probability) + "not possible.")
        noMutations = round(probability / self.__getRandomNumber(100))

        if noMutations > self.size:  # scramble
            first = self.__getRandomNumber(self.size)
            second = self.__getRandomNumber(self.size)
            (first, second) = \
                (min(first, second), max(first, second))
            for i in range(first, second):
                swapee = self.__getRandomNumber(first, second)
                (self.elements[i], self.elements[swapee]) = \
                    (self.elements[swapee], self.elements[i])

        else:  # possible multiple swaps
            while noMutations > 0:
                noMutations -= 1
                first = self.__getRandomNumber(self.size)
                second = self.__getRandomNumber(self.size)
                (self.elements[first], self.elements[second]) = \
                    (self.elements[second], self.elements[first])

    def combine(self, other):
        if not isinstance(other, Permutation):
            raise StatError("Cannot combine different types.")
        if self.size != other.size:
            raise StatError("Cannot combine permutations of different size.")
        firstCut = self.__getRandomNumber(self.size / 2)
        secondCut = round(firstCut + self.size / 2)
        for i in range(0, self.size):
            if firstCut < i < secondCut:
                other.elements[i] = self.elements[i]
        return other


    @staticmethod
    def __getRandomNumber(size):
        return round(random.uniform(0, size))

    @staticmethod
    def __getRandomNumber(first, second):
        return round(random.uniform(first, second))

    def _find0(self):
        """
        Returns index of first 0 in elements
        :return: integer
        """
        for index in range(0, self.size):
            if self.elements[index] == 0:
                return index
        return self.size

    def __str__(self):
        string = "Permutation :"
        for elem in self.elements:
            string += " " + str(elem)
        return string

