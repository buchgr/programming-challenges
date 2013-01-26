from collections import deque

class hopcroftgraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v1, v2, matched = False):
        if v1 not in self.graph:
            self.graph[v1] = {}
        if v2 not in self.graph:
            self.graph[v2] = {}

        self.graph[v1][v2] = matched
        self.graph[v2][v1] = matched

    def invert_matching_edge(self, v1, v2):
        # get the current state (matched / free)
        match = self.graph[v1][v2]
        # and invert it
        self.add_edge(v1, v2, not match)

    def free_vertices(self):
        vertices = set()
        for v,e in self.graph.iteritems():
            # check for matched edges
            if not any(e.values()):
                vertices.add(v)

        return vertices

    def matched_vertex(self, v):
        if not v in self.graph:
            raise Exception("The vertex '{0}' is not in the graph".format(v))

        return any(self.graph[v].values())

    def matching(self):
        m = set()
        for v,e in self.graph.iteritems():
            m |= set((v,x[0]) for x in e.items() if x[1] and (x[0],v) not in m)
        
        return m

    def neighbours(self, v):
        if not v in self.graph:
            raise Exception("No such vertice '{0}'".format(v))

        return self.graph[v]

    def vertices(self):
        return self.graph.keys()

    def __str__(self):
        return str(self.graph)

def bfs(G, V1):
    # put all free vertices from V1 into the queue
    q = deque(G.free_vertices() & V1)
    # initalize every vertice with -1
    level = {v: -1 for v in G.vertices()}
    
    for v in q:
        level[v] = 0
   
    phase_one = True
    # while the queue is not empty
    while q:
        # Phase 1 (the queue consists only of vertices of V1)
        if phase_one:
            qlen = len(q)

            for _ in xrange(qlen):
                # current vertice
                v = q.popleft()
                # get all neighbours connected via a free edge
                unmatched_nbrs = [e[0] for e in G.neighbours(v).items() if not e[1]]

                for w in unmatched_nbrs:
                    # the neighbour has not been visited by the BFS yet
                    if level[w] == -1:
                        level[w] = level[v] + 1
                        q.append(w)

            # alternate between the phases
            phase_one = False
        # Phase 2 (the queue consists only of vertices of V2)
        else:
            # If the queue contains a free vertex, then we found an
            # augmenting path and may stop the BFS
            for v in q:
                if not G.matched_vertex(v):
                    return level

            qlen = len(q)

            for _ in xrange(qlen):
                # current vertice
                v = q.popleft()
                matched_nbrs = [e[0] for e in G.neighbours(v).items() if e[1]] 

                for w in matched_nbrs:
                    # the neighbour has not been visited by the BFS yet
                    if level[w] == -1:
                        level[w] = level[v] + 1
                        q.append(w)

            # alternate between the phases
            phase_one = True

    # the queue is empty, we are done, no more augmenting paths
    return {}

def dfs(G, V1, V2, v, level):

    if v in V1:
        # for all nbrs of v that are connected via a free edge and level[w] - level[v] = 1 
        vertices = [e[0] for e in G.neighbours(v).items() if not e[1] and level[e[0]] == level[v] + 1]

        # no more ways to go? no problem
        # we'll just continue with the parent vertex
        # and mark this path as a dead end
        if not vertices:
            level[v] = -1
            return False

        for w in vertices:
            # did we find an augmenting path?
            if not G.matched_vertex(w):
                # if so, stop the dfs and start 
                # inverting the matching of this 
                # augmenting path
                G.invert_matching_edge(v,w)
                level[v] = -1
                return True
            else:
                if dfs(G,V1,V2,w,level):
                    G.invert_matching_edge(v,w)
                    level[v] = -1
                    return True
    # v is in V2
    else:
        # filter all neighbours connected via a matched edge
        vertices = [e[0] for e in G.neighbours(v).items() if e[1] and level[e[0]] == level[v] + 1]

        if not vertices:
            level[v] = -1
            return False

        for w in vertices:
            if dfs(G,V1,V2,w,level):
                G.invert_matching_edge(v,w)
                level[v] = -1
                return True

def maximum_matching(G, V1, V2):
    while True:
        level = bfs(G, V1)

        # if an augmenting path exists
        if level:
            # free vertices in V1
            free_vertices = V1 & G.free_vertices()
            for v in free_vertices:
                # do a DFS search for every free vertex
                dfs(G, V1, V2, v, level)

        # if no augmenting path exists, we are done
        # since a maximum matching has been found
        else:
            # return the matching as a list of tuples (v,w)
            return G.matching()
