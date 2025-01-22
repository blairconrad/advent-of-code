# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/23

import itertools
from collections import defaultdict
from functools import partial

from pipe import Pipe, select, where

from solutions.utils.iterables import how_many

from ...base import StrSplitSolution, answer

pairs = Pipe(itertools.combinations, 2)


def might_have_chief(cliques: tuple[str, str, str]) -> bool:
    return any(cliques | select(lambda n: n.startswith("t")))


def embiggen_cliques(cliques: list[set[str]], smaller_neighbours: dict[str, set[str]]) -> list[set[str]]:
    bigger_cliques = []
    while len(cliques) > 0:
        clique = cliques.pop()
        for node, neighbours in smaller_neighbours.items():
            if clique <= neighbours:
                bigger_cliques.append(clique | {node})
    return bigger_cliques


class Solution(StrSplitSolution):
    _year = 2024
    _day = 23

    @answer((1218, "ah,ap,ek,fj,fr,jt,ka,ln,me,mp,qa,ql,zg"))
    def solve(self) -> tuple[int, str]:
        cliques = []
        smaller_neighbours = defaultdict(set)
        self.debug(self.input)
        edges = self.input | select(partial(str.split, sep="-"))
        self.debug(edges)
        for edge in edges:
            if edge[0] > edge[1]:
                smaller_neighbours[edge[0]].add(edge[1])
            else:
                smaller_neighbours[edge[1]].add(edge[0])
            cliques.append(set(edge))
        self.debug(smaller_neighbours)
        self.debug(cliques)

        cliques = embiggen_cliques(cliques, smaller_neighbours)
        self.debug(cliques)
        num_thruples = how_many(cliques | where(might_have_chief))

        while len(cliques) > 1:
            cliques = embiggen_cliques(cliques, smaller_neighbours)
        return (num_thruples, ",".join(sorted(cliques[0])))
