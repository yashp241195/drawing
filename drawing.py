


from graphics import *
win = GraphWin('G',500,500)

def function():
    pt={'x':10,'y':10}
    P=Point(pt['x'],pt['y'])
    P.setFill("red")
    P.draw(win)

function()

#Lines

def DDALine(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    
    if dx > dy :
        step=dx
    else:
        step=dy
    xinc=float(dx)/float(step)
    yinc=float(dy)/float(step)
    x=x1
    y=y1
    for i in range(1,step):
        x+=xinc
        y+=yinc
        pt=Point(round(x),round(y))
        pt.setFill("green")
        pt.draw(win)


        
DDALine(10,10,30,320)

def BresenhamLine(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    
    p=2*dx-dy
    x=x1
    y=y1

    for x in range(x1,x2):
        if p>0:
            p+=2*(dy-dx)
            y+=1
        else: 
            p+=2*dy
            
          
        pt=Point(x,y)
        pt.draw(win)

BresenhamLine(10,10,320,30)

#Circles

def symmetry4foldXY(x,X,y,Y):
    pt=Point(X+x,Y+y)
    pt.draw(win)
    pt=Point(X-x,Y-y)
    pt.draw(win)
    pt=Point(X-x,Y+y)
    pt.draw(win)
    pt=Point(X+x,Y-y)
    pt.draw(win)
    
def symmetry4foldYX(x,X,y,Y):
    pt=Point(Y+y,X+x)
    pt.draw(win)
    pt=Point(Y-y,X+x)
    pt.draw(win)
    pt=Point(Y+y,X-x)
    pt.draw(win)
    pt=Point(Y-y,X-x)
    pt.draw(win)

def symmetry8fold(x,X,y,Y):
    symmetry4foldXY(x,X,y,Y)
    symmetry4foldYX(x,X,y,Y)
    

def MidpointCircle(X,Y,R):
    x=0
    y=R
    d=1-R
    while x< 0.7*R :
        x+=1
        Q=(2*x+3)
        if d>0:
            d+=Q+2*(1-y)
            y-=1
        else:
            d+=Q
        symmetry8fold(x,X,y,Y)

MidpointCircle(200,200,50)

def BresenhamCircle(X,Y,R):
    x=0
    y=R
    d=3-(2*R)
    while x<(0.7*R):
        x+=1
        Q=(4*x)+6
        if d>0:
            d+=Q+4*(1-y)
            y-=1
        else:
            d+=Q
        symmetry8fold(x,X,y,Y)
        
BresenhamCircle(100,100,50)
"""
#Mid point Algo:
>Find F(x,y)
>Find Inequality and Region where F(x,y)>0,F(x,y)>0
>Find the Critical Point d/dx(F(x,y)) and d/dy(F(x,y))
 using partial differntial
>At critcal point Behavoiur of curve will change
>If d/dx(F(x,y)) > d/dy(F(x,y)), means dx < dy ,
>if dy>dx than plot y and compute x using the parameter
 defind by mid point approach with take of of Inequality

"""

#mid point ellipse

def ellipse(a,b,X,Y):
    sa=a*a
    sb=b*b
    d=sb+sa*(0.25-b)
    x=0
    y=b
    while sa*(y-0.5)>sb*(x+1):
        Q=sb*(2*x+3)
        if d<0:
            d+=Q
        else :
            d+=Q+2*sa*(1-y)
            y-=1
        x+=1
        symmetry4foldXY(x,X,y,Y)

    sqXn=(x+0.5)**2
    sqYn=(y-1)**2
    d=(sb*sqXn)+(sa*sqYn)-(sa*sb)

    while y>=0:
        Q=sa*(3-2*y)
        if d<0:
            d+=Q+2*sb*(x+1)
            x+=1
        else:
            d+=Q
        y-=1
        symmetry4foldXY(x,X,y,Y)

        
ellipse(70,30,250,100)    



def symmetry4foldLine(xf,x,X,y,Y):
    pt=Point(X+x,Y+y)
    line=Line(pt,Point(X+xf,Y+500))
    line.setWidth(2)
    line.draw(win)

    pt=Point(X+x,Y-y)
    line=Line(pt,Point(X+xf,Y-500))
    line.setWidth(2)
    line.draw(win)

    pt=Point(X-x,Y-y)
    line=Line(pt,Point(X-xf,Y-500))
    line.setWidth(2)
    line.draw(win)

    pt=Point(X-x,Y+y)
    line=Line(pt,Point(X-xf,Y+500))
    line.setWidth(2)
    line.draw(win)

   
def hyperbola(X,Y,a,b):
    sa=a*a
    sb=b*b
  
    x=a
    y=0
    d=sb*(a+0.25)-sa
    
    while sa*y < abs(sb*x):
        if y>200:
            break
            
        
        Q=-sa*(2*y+3)
        if d>=0:
            d+=Q
        else:
            d+=Q+2*sb*(1+x)
            x+=1
            
        y+=1
        
        symmetry4foldXY(x,X,y,Y)

    if a>b:
        xf=(a/b)*(500-(Y-y))+X
        symmetry4foldLine(xf,x,X,y,Y)
 
    
hyperbola(250,250,70,50)



def parabola(a,X,Y):
    x=0
    y=0
    d=1-2*a
    while y<2*a:
        Q=(3+2*y)
        if d<0:
            d+=Q
        else:
            d+=Q-4*a
            x+=1
        y+=1
        pt=Point(x+X,y+Y)
        pt.draw(win)
        pt=Point(x+X,Y-y)
        pt.draw(win)

    d=(4*a*(x+1))-((y+0.5)**2)
    while y<320:
        Q=-4*a
        if d>0:
            d+=Q
        else:
            d+=Q+2*(1+y)
            y+=1
        x+=1
        pt=Point(x+X,y+Y)
        pt.draw(win)
        pt=Point(x+X,Y-y)
        pt.draw(win)
   
    
   
parabola(20,200,300)



#Curve Tracing



#Control points
X1=[10,150,100,300]
Y1=[10,50,70,300]

#Bezier Curve
#Speed of execution not only depends on number of iterations,
#but also depends on data structure which you are using 
#this demonstrate (recursion- stack(Linked List)) is worse for higher
#order computation than Arrays if SubStructure is not highly Optimized


#Iterative approach Simple but faster 
def bezierItr(x,y):
    u=0
    while u<1:
        U=u
        V=1-u
        x1= x[0]*U*U*U
        y1= y[0]*U*U*U
        
        x2= 3*x[1]*U*U*V
        y2= 3*y[1]*U*U*V

        x3= 3*x[2]*U*V*V
        y3= 3*y[2]*U*V*V

        x4= x[3]*V*V*V
        y4= y[3]*V*V*V

        
        xt= x1 + x2 + x3 + x4
        yt= y1 + y2 + y3 + y4

   
        pt=Point(xt,yt)
        pt.setFill("green")
        pt.draw(win)
        
        u+=0.001#change Accuracy here
   
    

bezierItr(X1,Y1)


#deCasteljau's Recurance relation efficient but slower
   
def deCasteljau(dp,Arr,n,i,u):
    if dp[n][i]!=0:
        return dp[n][i]
    if n==0 :
        dp[n][i]=Arr[i]
        return dp[n][i]
    else :
        dp[n][i]=(u)*deCasteljau(dp,Arr,n-1,i,u)+(1-u)*deCasteljau(dp,Arr,n-1,i+1,u)
        return dp[n][i]

def bezierRec(x,y):
    u=0
    print "Bezier Recursive Begin",time.ctime()
    while u<1:
       dp=[[0]*4,[0]*4,[0]*4,[0]*4]      
              
       xt=deCasteljau(dp,x,3,0,u)

       dp=[[0]*4,[0]*4,[0]*4,[0]*4]    
       yt=deCasteljau(dp,y,3,0,u)
       
       pt=Point(xt,yt)
       pt.setFill("red")
       pt.draw(win)
       u+=0.001#change Accuracy here
    print "Bezier Recursive End",time.ctime()


        
bezierRec(X1,Y1)


# B Spline Curve Using De Boor


X=[10,20,80,100,140,150]
Y=[10,80,70,130,120,150]



def N(n,t,i,k,u):
    if k==1:
        if u >= t[i] and u < t[i+1]:
            return 1
        else:
            return 0

    else:
        Pcoef=0
        Qcoef=0
        
        if t[i+k-1]==t[i]:
            Pcoef=0
        else:
            Pcoef=(u-t[i])/(t[i+k-1]-t[i])
            
        if t[i+k]==t[i+1]:
            Qcoef=0
        else:
            Qcoef=(t[i+k]-u)/(t[i+k]-t[i+1])
    
        return Pcoef*N(n,t,i,k-1,u) + Qcoef*N(n,t,i+1,k-1,u)



def Bspline(n,k,x,y):
    t=[0]*(n+k)
    # the relation b/w 't' and 'u' created in such a way
    # that by defining values of t 'u' will be effected
    for i in range(0,n+k):
        if i < k:
            t[i]=0
        if i >= k and i <= n:
            t[i]=i-k+1
        if i > n :
            t[i]=n-k+2
    print t
    u=1
    
    while u <= (n-k+2):
        xt=0
        yt=0
        for i in range(0,n):
            xt+=x[i]*N(n,t,i,k,u)
            yt+=y[i]*N(n,t,i,k,u)
        pt=Point(xt,yt)
        pt.setFill("blue")
        pt.draw(win)            
        u+=0.001

    for i in range(0,6):
        pt=Point(x[i],y[i])
        pt.setFill("red")
        pt.draw(win)
  


Bspline(5,4,X,Y)



win.getMouse()
win.close()























