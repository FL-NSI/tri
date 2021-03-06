def belong(n,t):
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False

def my_sum(t):
    res=t[0]
    for i in range(len(t)):
        res=res+t[i]
    return res

def greatest_in(t):
    res=t[0]
    for element in t:
        if element>res:
            res=element
    return res

def my_len(t):
    cpt=0
    for element in t:
        cpt=cpt+1
    return cpt


def map_double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def smallestin(t,i,j):
    res=t[i]
    for indice in range(i+1,j+1):
        if t[indice]<res:
            res=t[indice]
    return res

def swap(t,i,j):
    sauv=t[i]
    t[i]=t[j]
    t[j]=sauv

def remove(t,i):
    res=[0]*(len(t)-1)
    for j in range (len(t)):
        if j<i:
            res[j]=t[j]
        if j>i:
            res[j-1]=t[j]
    return res

def my_selection_sort(t):
    res=[0]*len(t)
    for i in range(len(t)):
        j=index_of_the_smallest(t)
        res=t[j]
        remove(t,j)

def index_of_the_smallest(t,i,j):
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j

def tri(t):
    for i in range(1, len(t)):
        T=t[i]
        j =i- 1
        while j>=0 and t[j]>T:
            t[j+1]=t[j]
            j=j-1
        t[j+1]= T
    return t

def test_tri():
    t=[5,9,7,2,3,10,47,15,50]
    return belong(9,t) and not belong(5,t)
    print("test_belong "+str(test_belong()))

def selection_sort_in_place(t):
    for i in range (len(t)):
        s=index_of_the_smallest(t,i,len(t)-1)
        if s>i:
            swap(t,i,s)
    return None

def insert(t,i):
    for current_index in range(i-1,-1,-1):
        if t[current_index] > t[current_index+1]:
            swap(t,current_index,current_index+1)
        else:
            break

def insertion_sort_in_place(t):
    for i in range(1,len(t)):
        insert(t,i)






