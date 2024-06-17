def get_max_depth(list,depth,index):
    child1 = index + 2**depth
    child2 = child1+1
    
    if list[child1] and list[child2] == 'null':
        print(depth)
    elif list[child1] and list[child2] != 'null':
        depth +=1
        get_max_depth(list,depth,child1)
    else:
        depth +=1
        get_max_depth(list,depth,child2)
    
root = [3,9,20,'null','null',15,7]
get_max_depth(root,0,0)