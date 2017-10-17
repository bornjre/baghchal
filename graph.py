def __init__():
    pass


#could be implement as sigleton since will be using only as 
#class type (without instancing)
class Graph(object):
    
    #valid walk steps for goat and tiger and jump for tiger with corresponding position
    #goats to be killed while jumping (class properties not instance one)
    WALKGRAPH = [
		 [1, 5, 6],[0, 2, 6],[1, 3, 6, 7, 8],[2, 4, 8],[3, 8, 9],
         [0, 6, 10],[0, 1, 2, 5, 7, 10, 11, 12],[2, 6, 8, 12],[2, 3, 4, 7, 9, 12, 13, 14],[4, 8, 14],
         [5, 11, 15],[6, 10, 12, 16],[6, 7, 8, 11, 13, 16, 17, 18],[8, 12, 14, 18],[8, 9, 13, 18, 19],
         [10, 16, 20],[10, 11, 12, 15, 17, 20, 21, 22],[12, 16, 18, 22],[12, 13, 14, 17, 19, 22, 23, 24],[14, 18, 24],
         [15, 16, 21],[16, 20, 22],[16, 17, 18, 21, 23],[18, 22, 24],[18, 19, 23]
         ]
    JUMPGRAPH = [
        [[10,12,2], [5,6,1]],
        [[11,3], [6,2]],
        [[0,10,12,14,4], [1,6,7,8,3]],
        [[1,13], [2,8]],
        [[2,12,14], [3,8,9]],
        [[15,7], [10,6]],
        [[16,18,8], [11,12,7]],
        [[5,17,9], [16,12,8]],
        [[6,16,18], [7,12,13]],
        [[7,19], [8,14]],
        [[0,20,22,12,2], [5,15,6,11,6]],
        [[1,21,13], [6,16,12]],
        [[2,0,10,20,22,24,14,4], [7,6,11,16,17,18,13,8]],
        [[3,11,23], [8,12,18]],
        [[4,2,12,22,24], [9,8,13,18,19]],
        [[5,17], [10,16]],
        [[6,18,8], [11,17,12]],
        [[7,15,19], [12,16,18]],
        [[8,6,16], [13,12,17]],
        [[9,17], [14,18]],
        [[10,22,12], [15,21,16]],
        [[11,23], [16,22]],
        [[12,10,20,24], [17,16,21,23]],
        [[13,21],[18,22]],
        [[14,12,22], [19,18,23]]
    ]
    @staticmethod
    def is_walk_valid(to, frm):
        key = 0
        for value in Graph.WALKGRAPH:
            if(key == frm):
                for k in value:
                    if k == to:
                        return True
            key = key + 1
        return False
    @staticmethod
    def is_jump_valid(to, frm):
        #print("jump")
        #print("to:from",to,frm)
        key = 0
        
        for value in Graph.JUMPGRAPH:
            print("key",key)
            if (key == frm):
                #print(key)
                #print("inside:",to,frm)
                k = 0
                for v in value[0]:
                    #print("debug near 5")
                    if (v == to):
                        #print("Debug:05")
                        #print("i am eating ", value[1][k])
                        return True, value[1][k]
                    k = k + 1
            key = key + 1
        return False, None