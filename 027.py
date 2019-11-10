for i in range(ord("x"),ord("z")+1):
    for j in range(ord("x"),ord("z")+1):
        if j!=i:
            for k in range(ord("x"),ord("z")+1):
                if i!=k and j!=k:
                    if i!=ord("x") and k!=ord("x") and k!=ord("z"):
                        print("\na-->%s\nb-->%s\nc-->%s"%(chr(i),chr(j),chr(k)))
                
