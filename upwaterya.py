a,b,c = map(int,input().split())
x1 =((-b+(b**2-4*a*c)**0.5)/(2*a))
x2 =((-b-(b**2-4*a*c)**0.5)/(2*a))
judge = b**2-4*a*c
if judge < 0:
    print('No real root')
elif x1==x2:
    print('Two same roots x={:.0f}'.format(x1))
else:
    print('Two different roots x1={:.0f} , x2={:.0f}'.format(x1,x2))
