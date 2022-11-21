#coor_list=eval(input())
coor_list=[(10,-14), (6,-20), (8,-16), (5,-15)]


middle12=[(coor_list[0][0]+coor_list[1][0])/2,(coor_list[0][1]+coor_list[1][1])/2]
middle23=[(coor_list[1][0]+coor_list[2][0])/2,(coor_list[1][1]+coor_list[2][1])/2]
middle34=[(coor_list[2][0]+coor_list[3][0])/2,(coor_list[2][1]+coor_list[3][1])/2]
#middle41=[(coor_list[3][0]+coor_list[0][0])/2,(coor_list[3][1]+coor_list[0][1])/2]
area_quad=abs(((middle12[0]*middle23[1])+(middle23[0]*middle34[1])+(middle34[0]*middle12[1]))-((middle12[1]*middle23[0])+(middle23[1]*middle34[0])+(middle34[1]*middle12[0])))*2

min_list=[]
max_list=[]
#detect the min x and min_index
if coor_list[0][0]<=coor_list[1][0] and coor_list[0][0]<=coor_list[2][0] and coor_list[0][0]<=coor_list[3][0]:
    x_min=coor_list[0]
    x_min_index=0
    min_list.append(x_min)
    min_list.append(x_min_index)
if coor_list[1][0]<=coor_list[0][0] and coor_list[1][0]<=coor_list[2][0] and coor_list[1][0]<=coor_list[3][0]:
    x_min=coor_list[1]
    x_min_index=1
    min_list.append(x_min)
    min_list.append(x_min_index)
if coor_list[2][0]<=coor_list[0][0] and coor_list[2][0]<=coor_list[1][0] and coor_list[2][0]<=coor_list[3][0]:
    x_min=coor_list[2]
    x_min_index=2
    min_list.append(x_min)
    min_list.append(x_min_index)
if coor_list[3][0]<=coor_list[0][0] and coor_list[3][0]<=coor_list[1][0] and coor_list[3][0]<=coor_list[2][0]:
    x_min=coor_list[3]
    x_min_index=3
    min_list.append(x_min)
    min_list.append(x_min_index)

if len(min_list)==4:
    if min_list[0][1]>min_list[2][1]:
        x_min=min_list[2]
        x_min_index=min_list[3]
    else:
        x_min=min_list[0]
        x_min_index=min_list[1]
#detect the max x
if coor_list[0][0]>=coor_list[1][0] and coor_list[0][0]>=coor_list[2][0] and coor_list[0][0]>=coor_list[3][0]:
    x_max=coor_list[0]
    x_max_index=0
    max_list.append(x_max)
    max_list.append(x_max_index)
if coor_list[1][0]>=coor_list[0][0] and coor_list[1][0]>=coor_list[2][0] and coor_list[1][0]>=coor_list[3][0]:
    x_max=coor_list[1]
    x_max_index=1
    max_list.append(x_max)
    max_list.append(x_max_index)
if coor_list[2][0]>=coor_list[0][0] and coor_list[2][0]>=coor_list[1][0] and coor_list[2][0]>=coor_list[3][0]:
    x_max=coor_list[2]
    x_max_index=2
    max_list.append(x_max)
    max_list.append(x_max_index)
if coor_list[3][0]>=coor_list[0][0] and coor_list[3][0]>=coor_list[1][0] and coor_list[3][0]>=coor_list[2][0]:
    x_max=coor_list[3]
    x_max_index=3
    max_list.append(x_max)
    max_list.append(x_max_index)

"""
from operator import itemgetter
x_min=min(coor_list,key=itemgetter(0))
print(x_min)
x_max=max(coor_list,key=itemgetter(0))     # if we cannot use any library
print(x_max)
y_min=min(coor_list,key=itemgetter(1))
print(y_min)
y_max=max(coor_list,key=itemgetter(1))
print(y_max)

#detect the min y
if coor_list[0][1]<coor_list[1][1] and coor_list[0][1]<coor_list[2][1] and coor_list[0][1]<coor_list[3][1]:
    y_min=coor_list[0]
    y_min_index=0
elif coor_list[1][1]<coor_list[0][1] and coor_list[1][1]<coor_list[2][1] and coor_list[1][1]<coor_list[3][1]:
    y_min=coor_list[1]
    y_min_index=1
elif coor_list[2][1]<coor_list[0][1] and coor_list[2][1]<coor_list[1][1] and coor_list[2][1]<coor_list[3][1]:
    y_min=coor_list[2]
    y_min_index=2
else:
    y_min=coor_list[3]
    y_min_index=3

#detect the max y
if coor_list[0][1]>coor_list[1][1] and coor_list[0][1]>coor_list[2][1] and coor_list[0][1]>coor_list[3][1]:
    y_max=coor_list[0]
    y_max_index=0
elif coor_list[1][1]>coor_list[0][1] and coor_list[1][1]>coor_list[2][1] and coor_list[1][1]>coor_list[3][1]:
    y_max=coor_list[1]
    y_max_index=1
elif coor_list[2][1]>coor_list[0][1] and coor_list[2][1]>coor_list[1][1] and coor_list[2][1]>coor_list[3][1]:
    y_max=coor_list[2]
    y_max_index=2
else:
    y_max=coor_list[3]
    y_max_index=3
"""

indexs=[0,1,2,3]
indexs.remove(x_max_index)
indexs.remove(x_min_index)

#equation of the line
m=(abs(x_max[1])-abs(x_min[1]))/(x_max[0]-x_min[0])
bottom_area=(abs(coor_list[x_max_index][1])+abs(coor_list[x_min_index][1]))*abs(coor_list[x_max_index][0]-coor_list[x_min_index][0])/2
print("bottom",bottom_area)





#both higher than line
if abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if abs(coor_list[indexs[0]][1])<abs(coor_list[indexs[1]][1]):
            bottom_point=coor_list[indexs[0]]
        else:
            
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area+=triangle
    print("hi1")
    print(bottom_area)    

#both lower than line #works
elif abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if coor_list[indexs[0]][1]>coor_list[indexs[1]][1]:
            bottom_point=coor_list[indexs[0]]
        else:
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area-=triangle
    print("hi2")    
    print(bottom_area-area_quad)
    


else:
    if coor_list[indexs[0]][1]>coor_list[indexs[1]][1]:
        bottom_point=coor_list[indexs[1]]
    else:
        bottom_point=coor_list[indexs[0]]
    print(bottom_point)
    triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
    bottom_area-=triangle
    print("triangle:",triangle)
    print("hi3")
    print(bottom_area)