import sys

def exclude(vote1, vote2):
    '''tests whether two votes exclude one another'''

    # vote2 wants vote1's favorite pet out or vice versa?
    return vote1[0] == vote2[1] or vote2[0] == vote1[1]

def build_adjacency_matrix(votes):
    '''accepts a list of votes as tuples (love animal, hate animal)
       and represents each vote as a node in a graph. Two nodes are 
       connected if they do not exclude each other. The function returns
       an adjacency matrix of the graph.'''

    # initialize the matrix
    matrix = []
    N = len(votes)
    for i in xrange(N):
        # initalize the row with False
        matrix.append([False] * N)

    for i in xrange(N):
        for j in xrange(N):
            # connect the nodes if the corresponding
            # votes do not exclude each other
            if not exclude(votes[i], votes[j]):
                matrix[i][j] = matrix[j][i] = True

    return matrix

def build_new(connected, c, arr):
    return [x for x in arr if connected[c][x]]

def algorithm457(connected, candidates, processed=None, compsub=None):
    '''implementation of the Bron-Kerbosch Algorithm for finding maximum
       cliques in undirected graphs'''

    if processed is None:
        processed = set()
    if compsub is None:
        compsub = set()

    num_cand = len(candidates)
    maxedges = -1
    pivot = -1
    for p in processed:
        edges = 0
        for c in candidates:
            if connected[p][c]:
                edges += 1

        if edges > maxedges:
            maxedges = edges
            pivot = p 
            # if a node in "processed" is connect to every
            # node in candidate, we know that these candidates
            # won't form a maximum clique, since this clique
            # would have already been found previously
            if edges == num_cand:
                return

    for p in candidates:
        edges = 0
        for c in candidates:
            if connected[p][c]:
                edges += 1

        if edges > maxedges:
            maxedges = edges
            pivot = p

    smaller_candidates = set(x for x in candidates if connected[pivot][x])
    
    # size of the biggest clique found
    max_clique = 0
    for c in smaller_candidates:
        candidates.remove(c)
        compsub.add(c)

        # remove all nodes from processed and candidates that are not connected to c
        new_processed  = set(x for x in processed if connected[c][x])
        new_candidates = set(x for x in candidates if connected[c][x])

        if not new_processed and not new_candidates:
            max_clique = max(max_clique, len(compsub))
        elif not new_processed and len(new_candidates) is 1:
            max_clique = max(max_clique, len(compsub)+1)
        else:
            max_clique = max(max_clique, algorithm457(connected, 
                                                      new_candidates,
                                                      new_processed,
                                                      compsub))

        processed.add(c)
        compsub.remove(c)

    return max_clique

# number of testcases
testcases = int(raw_input())
# list of maximum clique size per testcase
cliques = []

for _ in xrange(testcases):
    # number of cats, dogs and voters
    cats, dogs, voters = [int(num) for num in raw_input().split(" ")]

    # process votes and build an adjacency matrix from them
    # Two votes are connected if they do not exclude each other
    votes = []
    for __ in xrange(voters):
        love, hate = [vote.strip() for vote in raw_input().split(" ")]
        votes.append((love, hate))

    connected = build_adjacency_matrix(votes)

    # Run the Bron-Kerbosch Algorithm (CACM's Algorithm 457)
    # The algorithm returns the maximum cardinality of all the
    # maximum cliques found.
    max_clique = algorithm457(connected, set(range(len(votes))))

    cliques.append(max_clique)

# Print the results and make sure that
# the last line does not end with a line break
N = len(cliques)
for i in xrange(N-1):
    print cliques[i]

sys.stdout.write(str(cliques[N-1]))
