def solution(m):

    # Calculate map stats
    w, h = len(m[0]), len(m) # width and height
    
    # The current minimal solution
    s_min = 401

    # Iterate over all possible inputs (by replacing 1s with 0s).
    for m_0 in all_maps(m):
        shortest_lengrh = min_path(m_0, w, h)
        print 'shortest_lengrh',shortest_lengrh
        # Find the minimal path length
        s_min = min(shortest_lengrh, s_min)
        print 's_min',s_min
        # Optimization: Minimal solution?
        if s_min == w + h - 1:
            return s_min
        
    return s_min


def min_path(m, w, h):
    '''Takes a map m and returns the minimal path
    from the start to the end node. Also pass width and height.
    '''
        
    # Initialize dictionary of path lengths
    # integer: {(i,j), ...} (Set of nodes (i,j) with this integer path length)
    d = {1: {(0,0)}}

    # Expand "fringe" successively
    path_length = 2
    while path_length < 401 and d[path_length-1]:
        # Fill fringe
        fringe = set()
        for x in d[path_length-1]:
            if path_length-1 == 5:
                print 'd in index:',path_length-1,'is x:',x,'which has neighbors:',neighbors(x,m)
            # Expand node x (all neighbors) and exclude already visited
            expand_x = {y for y in neighbors(x,m) if not any(y in visited for visited in d.values())}
            fringe = fringe | expand_x

        # Have we found min path of exit node?
        if (h-1, w-1) in fringe:
            print 'd.values',d.values()
            return path_length
        
        # Store new fring of minimal-path nodes
        d[path_length] = fringe

        # Find nodes with next-higher path_length
        path_length += 1
        print path_length

    return 401 # Infinite path length  

def neighbors(x, m):
    '''Returns a set of nodes (as tuples) that are neighbors of node x in m.'''
    i, j = x
    w, h = len(m[0]), len(m)
    candidates = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
    neighbors = set()
    for y in candidates:
        i, j = y
        if i>=0 and i<h and j>=0 and j<w and m[i][j] == 0:
            neighbors.add(y)
    
    return neighbors


def all_maps(m):
    '''Returns an iterator for memory efficiency
    over all maps that arise by replacing a '1' with a '0' value.'''

    # Unchanged map is a valid solution
    yield m

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]:
                # Copy the map
                copy = [[col for col in row] for row in m]

                # Replace 1 by 0 and yield new map
                copy[i][j] = 0
                yield copy
l = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print solution(l)