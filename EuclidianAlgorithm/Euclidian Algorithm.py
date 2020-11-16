'''
def dist2(x1,y1,x2,y2):
    dx=x1-x2
    dy=y1-y2
    dist=(dx**2+dy**2)**0.5
    return dist

def area3(x1,y1,x2,y2,x3,y3):
    a=dist2(x1,y1,x2,y2)
    b=dist2(x2,y2,x3,y3)
    c=dist2(x3,y3,x1,y1)
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c)**0.5)
    return area

print(area3(0,0,1,4,3,7))
'''

#Euclidean Algorithm:

def euclideanAlgorithm(p,q):
    while p != q:
        if p > q:
            p = p-q
        else:
            q = q-p
    return(p,q)


print(euclideanAlgorithm(20, 19))
print(euclideanAlgorithm(27, 22))
print(euclideanAlgorithm(38, 18))
print(euclideanAlgorithm(13, 9))
print(euclideanAlgorithm(7, 3))

