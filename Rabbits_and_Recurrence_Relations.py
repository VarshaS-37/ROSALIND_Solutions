no=list(map(int,input().split()))
month=no[0]
pairs=no[1]
def fib(month,pairs):
    if month==1:
        return 1
    elif month<=0:
        return 0
    else:
        return(fib(month-1,pairs)+pairs*fib(month-2,pairs))
print(fib(month,pairs))