# I modelled this problem as a bipartite graph
# where each vote is a vertex. All votes in favor of cats 
# go on one side and all votes in favor of dogs go to the other
# side of the graph.
# Two vertices/votes are connected if they exclude one another,
# in a way that they cannot both be satisfied (e.g. C1 D1 and D1 C1)
#
# Then I apply the Hopcroft-Karp algorithm to calculate a maximum
# matching.
#
# The idea behind using the Hopcroft-Karp algorithm is as follows:
# Each set of votes contains at least one "biggest group of 
# non-excluding votes". Each vote that is not in this group collides
# with at least one vote in the group, otherwise it would be in
# that group itself. So for every vote colliding with some vote
# from the biggest group, the matching increases by one. Therefore
# the maximum matching has the same size as the total number of
# collissions between the biggest group and every vote not in it and
# that again is the number of votes NOT in the "biggest group of
# non-excluding votes".
# Therefore |all votes| - |maximum matching| = |biggest group of non-excluding-votes|
# 
import sys

from hopcroftkarp import hopcroftgraph, maximum_matching

def build_graph(votes):
    V1 = set()
    V2 = set()
    G = hopcroftgraph()

    N = len(votes)
    for i in range(N):
        love1, hate1 = votes[i]
        vertex1 = "#%d %s %s" % (i, love1, hate1)
        
        # cat votes to the left
        if love1[0] == 'C':
            V1.add(vertex1)
        # dog votes to the right
        else:
            V2.add(vertex1)

        for j in range(N):
            love2, hate2 = votes[j]
            if love1 == hate2 or love2 == hate1:
                vertex2 = "#%d %s %s" % (j, love2, hate2)
                G.add_edge(vertex1, vertex2) 

    return (G, V1, V2)

# number of testcases
testcases = int(raw_input())

results = []

for _ in range(testcases):
    # number of cats, dogs and voters
    cats, dogs, voters = [int(num) for num in raw_input().split(" ")]

    votes = []
    for _ in range(voters):
        love, hate = [vote.strip() for vote in raw_input().split(" ")]
        votes.append((love,hate))

    graph = build_graph(votes)
    result = voters - len(maximum_matching(*graph))
    results.append(result)

N = len(results)
for i in range(N-1):
    sys.stdout.write("%d\n" % results[i])
sys.stdout.write("%d" % results[N-1])
