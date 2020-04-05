def bfs(G, s, cb):
    visited = {s: True}
    q = [s]

    while q:
        x = q.pop(0)
        #################################
        # Callback function for each node
        if cb:
            cb(x)
        #################################
        for n in G[x]:
            if not visited[n]:
                visited[n] = True
                q.append(n)