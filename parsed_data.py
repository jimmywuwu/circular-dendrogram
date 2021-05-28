from collections import deque,defaultdict

class TreeNode:
    def __init__(self,layer,child_num,node_id):
        self.layer=layer
        self.node_id=node_id
        self.child_num=child_num
        self.child=[]

    def add(self,nodes):
        self.child.extend(nodes)

def parsed_data(tree):
    # parsed data from tree list 
    all_layer=[]
    layer=[]
    for i in range(len(tree)-1):
        if tree[i][0]>tree[i+1][0]:
            layer.append(tree[i][1])
            all_layer.append(layer)
            layer=[]
            continue
        layer.append(tree[i][1])

    # initialize nodes to generate hierarchical tree
    nodes=deque([(TreeNode(layer=0,child_num=1,node_id=node_id),group) for node_id,group in enumerate(all_layer[0])])

    # start iteration
    layer_num=0
    while layer_num<len(all_layer)-1:
        node_num=len(all_layer[layer_num])
        collect_dict=defaultdict(list)
        while node_num>0:
            node,group=nodes.popleft()
            collect_dict[group].append(node)
            node_num-=1
        
        for node_id,group in enumerate(all_layer[layer_num+1]):
            node_next_layer=TreeNode(layer=layer_num+1,child_num=sum([node.child_num for node in collect_dict[node_id]]),node_id=node_id)
            node_next_layer.add(collect_dict[node_id])
            nodes.append((node_next_layer,group))
        
        layer_num+=1

    root=TreeNode(layer=len(all_layer)+1,child_num=len(all_layer[0]),node_id=0)
    root.add([group[0] for group in nodes])
    return root