import math
class CircularDendrogram:
    def __init__(self,root,terminate_layer=0,r_add=1):
        self.Xv=[]
        self.Yv=[]
        self.Xed=[]
        self.Yed=[]
        self.idx=0
        self.terminate_layer=terminate_layer
        self.node_num=self.get_node_num(root,terminate_layer)
        self.r_add=r_add
        self.dfs(root,0)

    def dfs(self,root,r):
        if root.layer==self.terminate_layer:
            # calculate node position
            theta=self.idx*2*3.1415926/self.node_num
            x=r*math.cos(theta)
            y=r*math.sin(theta)
            self.Xv.append(x)
            self.Yv.append(y)
            self.idx+=1
            return x,y
        
        start_idx=self.idx
        Xed_update=[]
        Yed_update=[]
        for child in root.child:
            # add node position here
            child_x,child_y=self.dfs(child,r+self.r_add)
            Xed_update.append([0,child_x,None])
            Yed_update.append([0,child_y,None])
        end_idx=self.idx
        theta=(start_idx+end_idx)//2*2*3.1415926/self.node_num
        x=r*math.cos(theta)
        y=r*math.sin(theta)
        self.Xv.append(x)
        self.Yv.append(y)
        for i in range(len(Xed_update)):
            Xed_update[i][0]=x
            Yed_update[i][0]=y
        
        self.Xed.extend([i  for j in Xed_update for i in j])
        self.Yed.extend([i for j in Yed_update for i in j])

        return x,y

    def get_node_num(self,root,layer):
        if root.layer==layer:
            return 1
            
        return sum([self.get_node_num(child,layer) for child in root.child])
