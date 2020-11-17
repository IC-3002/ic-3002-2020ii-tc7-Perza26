def encontrar_ruta(C):
    n = len(C)
    m = len(C[0])
    solve = [[0 for x in range(m)] for y in range(n)]
    if encontrar_ruta_aux(C,solve,0,0)==False:
        return []
    return solve

def encontrar_ruta_aux(C,solve,n,m):
    x=len(C)-1
    y=len(C[0])-1
    print(solve)
    if((n==x) and (m==y) and C[n][m]==0):
        solve[n][m]=1
        return True
    if(n>=0 and n<x+1 and m>=0 and m<y+1 and C[n][m]==0 and solve[n][m]==0):
        solve[n][m]=1   
        if((encontrar_ruta_aux(C,solve,n,m+1))):
                return True
        if((encontrar_ruta_aux(C,solve,n+1,m))):
                return True
        if((encontrar_ruta_aux(C,solve,n,m-1))):
                return True
        if((encontrar_ruta_aux(C,solve,n-1,m))):
                return True
        solve[n][m]=0
        return False