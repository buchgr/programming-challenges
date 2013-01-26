import sys

from hopcroftkarp import hopcroftgraph, maximum_matching

def build_graph(votes):
    V1 = set()
    V2 = set()
    G = hopcroftgraph()

    N = len(votes)
    for i in xrange(N):
        love1, hate1 = votes[i]
        vertex1 = "#%d %s %s" % (i, love1, hate1)
        
        # cat votes to the left
        if love1[0] == 'C':
            V1.add(vertex1)
        # dog votes to the right
        else:
            V2.add(vertex1)

        for j in xrange(N):
            love2, hate2 = votes[j]
            if love1 == hate2 or love2 == hate1:
                vertex2 = "#%d %s %s" % (j, love2, hate2)
                G.add_edge(vertex1, vertex2) 

    return (G, V1, V2)

# number of testcases
testcases = int(raw_input())

results = []

for _ in xrange(testcases):
    # number of cats, dogs and voters
    cats, dogs, voters = [int(num) for num in raw_input().split(" ")]

    votes = []
    for _ in xrange(voters):
        love, hate = [vote.strip() for vote in raw_input().split(" ")]
        votes.append((love,hate))

    graph = build_graph(votes)
    result = voters - len(maximum_matching(*graph))
    results.append(result)

N = len(results)
for i in xrange(N-1):
    sys.stdout.write("%d\n" % results[i])
sys.stdout.write("%d" % results[N-1])
