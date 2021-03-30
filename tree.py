import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import numpy as np
from expectimax import expectiminimax
import sys

sys.setrecursionlimit(1500000)


def get_node_name(state):
    return "%0.2f"%state

max_depth = 3
total_winning = np.zeros(max_depth)
total_losing = np.zeros(max_depth)

def add_node_ob(G,state,r, max_depth, current_depth = 1):
    global total_winning
    global total_losing

    win = r+r*.5
    lose = r - r * .4

    w = get_node_name(win) #+ "\n" + get_node_name(np.random.random())
    l = get_node_name(lose)# + "\n" + get_node_name(np.random.random())
    G.add_node(w)
    G.add_node(l)

    G.add_edge(state,w)
    G.add_edge(state,l)

    if(current_depth < max_depth ):
        add_node_ob(G,w,win, max_depth, current_depth+1)
        add_node_ob(G,l,lose, max_depth, current_depth + 1)

    if(win > 10):
        total_winning[current_depth-1]+=1
    else:
        total_losing[current_depth-1]+=1

    if (lose > 10):
        total_winning[current_depth-1] += 1
    else:
        total_losing[current_depth-1] += 1



def add_node(G,state,max_depth, current_depth = 1):

    #print(current_depth)
    win = state+state*.5
    lose = state - state * .4
    v = (0.5*win + 0.5*lose) - state

    play_node = "Play %s" % (get_node_name(state))
    stop_node = "Stop %s" % (get_node_name(state))
    G.add_node(play_node, action_node = False)
    G.add_node(stop_node, action_node = False)

    G.add_edge(get_node_name(state), play_node, label = "Play")
    G.add_edge(get_node_name(state), stop_node, label = "Stop")

    G.add_node(get_node_name(win), action_node = True)
    G.add_node(get_node_name(lose), action_node = True)

    G.add_edge(play_node, get_node_name(win), label = "R = " +  get_node_name(state*0.5),R = 0.5*state)
    G.add_edge(play_node, get_node_name(lose), label = "R = " +  get_node_name(-state*0.4), R = -0.4*state)

    if(current_depth < max_depth ):
        add_node(G,win, max_depth, current_depth+1)
        add_node(G,lose, max_depth, current_depth + 1)

    if (win > 10):
        total_winning[current_depth - 1] += 1
    else:
        total_losing[current_depth - 1] += 1

    if (lose > 10):
        total_winning[current_depth - 1] += 1
    else:
        total_losing[current_depth - 1] += 1

def main():
    G = nx.DiGraph()
    add_node(G, 10.0,max_depth)
    #add_node_ob(G, get_node_name(10.0),10.0,max_depth)
    #G.add_node(get_node_name(10.0))
    print(list(G.successors(get_node_name(10.0))))
    G.nodes[get_node_name(10.0)]["action_node"] = True
    ed = G.out_edges(get_node_name(10.0))
    print(ed)
    print(G.edges[list(ed)[0]])
    print(G.nodes[get_node_name(10)])
    print(len(list(G.nodes())), "all nodes size")

    print(total_winning/(total_winning+ total_losing))
    try:
        nx.nx_agraph.write_dot(G, './plots/tree.dot')
    except:
        print("Casual crush")

    a = expectiminimax(G,get_node_name(10.0) )
    print(a)

    #
    # # same layout using matplotlib with no labels
    # plt.title('draw_networkx')
    # pos = graphviz_layout(G, prog='dot')
    # nx.draw(G, with_labels=True, arrows=True)
    # plt.savefig('nx_test.png')


if __name__ == "__main__":
    main()