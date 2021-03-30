import numpy as np

def expectiminimax(G, node, cache = None):
    #print("Top node", node)
    out_edges = list(G.out_edges(node))
    action_node = G.nodes[node]["action_node"]

    if(cache is None):
        cache = {}

    children = [out_edge[-1] for out_edge in out_edges]
    is_terminal = len(children) == 0
    #print("is terminal", is_terminal)
    #print(depth)
    if is_terminal:
        return 0.0
    elif action_node:
        a = -np.inf
        arg_a = -1
        for i, child in enumerate(children):
            #print("max child", child, a)
            if(child in cache):
                result = cache[child]
            else:
                result = expectiminimax(G,child, cache)
                cache[child] = result


            if(result > a):
                a = result
                arg_a = i
            #a = np.max([a, ])
        #print(node, arg_a)
        G.nodes[node]["value"] = a

    else:
        # Return weighted average of all child nodes' values
        a = 0
        for i,child in enumerate(children):
            #print(out_edges)
            rewards = [G.edges[out_edge]["R"] for out_edge in out_edges]
            if (child in cache):
                result = cache[child]
            else:
                result = expectiminimax(G,child, cache)
                cache[child] = result

            rew = rewards[i]
            rest = (0.5 * (result+rew))
            #print(i,"rewards", rewards, a, rest, exp, rew)
            a = a + rest


        G.nodes[node]["value"] = a
        #print(a)
    return a