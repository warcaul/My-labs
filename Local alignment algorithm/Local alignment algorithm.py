A = 'ACGGATTACTCAGCTACGCTCGACTACTGACTGTGCATGCATGCTGCGCGCTAGCGCTCGCTAGCGACGAGCTACGATCTAGCGACGTACTGACGTAAAAAAACGATCGAATG'
B = 'ACTGATCGTG'

ma = 1
mi = 0
g  = -1
def getMatrix(X , Y):
    matrix = []
    for i in range(len(Y) + 1):
        submatrix = []
        for j in range (len(X) + 1):
            submatrix.append(0)
        matrix.append(submatrix)
    return matrix

def TBmatrix(X, Y):
    matrix = []
    for i in range(len(Y) + 1):
        submatrix = []
        for j in range (len(X) + 1):
            submatrix.append(0)
        matrix.append(submatrix)
    
    for l in range(1 , len(X) + 1):
        matrix[0][j] = 'left'
    for i in range(1 , len(Y) + 1):
        matrix[i][0] = 'up'
    matrix[0][0] = 'done'
    return matrix

def TBmetod (X , Y):    
    mat = getMatrix(X, Y)
    TBmat = TBmatrix(X , Y)
    best = 0
    optLoc = (0,0)
    for i in range(1 , len(Y) + 1):
        for j in range(1 , len(X) + 1):
            left = mat[i][j-1] + g
            up = mat[i-1][j] + g
            diag = mat[i-1][j-1] + (ma if X[j-1] == Y[i-1] else mi)
            mat[i][j] = max(left, up, diag, 0)
            if mat[i][j] == left:
                TBmat[i][j] = 'left'
            elif mat[i][j] == up:
                TBmat[i][j] = 'up'
            elif mat[i][j] == diag:
                TBmat[i][j] = 'diag'
            else:
                TBmat[i][j] = '0'
            if  mat[i][j] >= best:
                best = mat[i][j]
                optLoc = (i , j)
    return  best, optLoc, mat, TBmat

def localAlign(X, Y):

    best, optLoc, mat, TBmat = TBmetod (X , Y)
    
    seq1 = ' '
    seq2 = ' '
    i = optLoc[0]
    j = optLoc[1]
    
    while (i > 0 or j > 0):
        if TBmat[i][j] == 'diag':
            seq1 += X[j-1]
            seq2 += Y[i-1]
            i -= 1
            j -= 1
        elif TBmat[i][j] == 'left':
            j -= 1
        elif TBmat[i][j] == 'up':   
             i -= 1
        elif TBmat[i][j] == 'done':
            break                
        else:
            break
    return seq1[::-1] , seq2[::-1], optLoc


a = localAlign(A, B)

print((a[2][1] - len(a[0])+1) ,'-', a[0] ,'-', a[2][1] + 1 )
print((a[2][0] - len(a[1])+1) ,'-', a[1] ,'-', a[2][0] + 1 )



