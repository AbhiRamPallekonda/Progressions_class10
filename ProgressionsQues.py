l=list(map(int,input("Enter a series of numbers: ").split(",")))
n=len(l)
ap=[]
gp=[]
for i in range(0,n):
    if i!=n-1:
        ap.append(l[i+1]-l[i])
        gp.append(l[i+1]/l[i])
if ap.count(ap[0])==len(ap):
    print("This is Arithmetic progression")
    print("D :",int(l[1]-l[0]))
    a=l[0]
    an=int(l[-1])
    s=(n/2)*(a+an)
    print("Sum :",int(s))
elif gp.count(gp[0])==len(gp):
    print("This is geometric progression")
    r=l[1]/l[0]
    a=l[0]
    if abs(r)<1:
        print("r :",r)
        print("|r|<1. So, sn :",a/(1-r))
    else:
        print("r :",r)
        an=int(l[-1])
        s=(((a)*((r**n)-1))/(r-1))
        print("Sum :",s)