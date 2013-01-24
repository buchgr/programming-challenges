import sys
import networkx as nx

def exclude(vote1, vote2):
    '''tests whether two votes exclude one another'''

    # vote2 wants vote1's favorite pet out or vice versa?
    return vote1[0] == vote2[1] or vote2[0] == vote1[1]

def build_graph(votes):
    G = nx.Graph()
    G.add_nodes_from(range(len(votes)))
    N = len(votes)
    for i in xrange(N):
        for j in xrange(N):
            if not exclude(votes[i], votes[j]):
                G.add_edge(i,j)

    return G

# number of testcases
testcases = int(raw_input())
# list of maximum clique size per testcase
cliques = []

for _ in xrange(testcases):
    # number of cats, dogs and voters
    cats, dogs, voters = [int(num) for num in raw_input().split(" ")]

    votes = []
    for __ in xrange(voters):
        love, hate = [vote.strip() for vote in raw_input().split(" ")]
        votes.append((love, hate))

    G = build_graph(votes)
    cliques.append(max(map(len, list(nx.find_cliques(G)))))

# Print the results and make sure that
# the last line does not end with a line break
N = len(cliques)
for i in xrange(N-1):
    print cliques[i]

sys.stdout.write(str(cliques[N-1]))
