from parsed_data import parsed_data
from Dendrogram import CircularDendrogram
from plotly.graph_objects import *


if __name__=='__main__':
    with open('graph.tree','r') as f:
        tree=f.read()
    tree=tree[:-1]
    tree=[[int(j) for j in element.split(' ')] for element in tree.split('\n')]

    # parsing data
    root=parsed_data(tree)

    # Layout circular dendrogram
    cd=CircularDendrogram(root,terminate_layer=1)

    # Plotting with plotly
    trace1=Scatter(x=cd.Xv,
                y=cd.Yv,
                mode='markers',
                name='node_on_cg',
                marker=dict(symbol='circle',
                                size=1,
                                color='red',
                                line=dict(color='rgb(50,50,50)', width=0),
                                ),
                )
    trace2=Scatter(x=cd.Xed,
                y=cd.Yed,
                mode='lines',
                line=dict(color='rgb(210,210,210)', width=1),
                hoverinfo='none',
                name='edge'
                )

    fig=Figure([trace1,trace2],layout=Layout(width=2000,height=2000))
    fig.show()
