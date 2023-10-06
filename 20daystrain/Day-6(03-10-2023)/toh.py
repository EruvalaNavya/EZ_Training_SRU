def toh(n,src,aux,dest):
    if(n==1):
        print( n," from ",src," to ",dest)
        return
    toh(n-1,src,dest,aux)
    print(n," from ",src," to ",dest)
    toh(n-1,aux,src,dest)
n=int(input())
toh(n,'src','aux','dest')

