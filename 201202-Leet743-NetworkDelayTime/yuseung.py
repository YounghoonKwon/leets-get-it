class Solution(object):
    def networkDelayTime(self, times, N, K):
		
		# Record the edge info and corresponding cost
        edge = collections.defaultdict(list)
        cost = {}
        for time in times:
            edge[time[0]].append(time[1])
            cost[(time[0], time[1])] = time[2]
        
		# bfs keeps records of the cost from origin node to each node
        bfs = {K:0}
        level = [K]
        for x in level:
            for y in edge[x]:
                if y not in bfs:
                    bfs[y] = bfs[x] + cost[(x,y)]
                    level.append(y)
				# Note: here if the cost to node y decrease, we need to revisit y and update the costs to all of y's childs
                else:
                    if bfs[x] + cost[(x,y)] < bfs[y]:
                        bfs[y] = bfs[x] + cost[(x,y)]
                        level.append(y)
        return max(bfs.values()) if len(bfs) == N else -1
