#coor_list=eval(input())
coor_list=[(12.5,11.3), (2.0,12.0), (18.7,16.2), (12.5,7.0)]



middle12=[(coor_list[0][0]+coor_list[1][0])/2,(coor_list[0][1]+coor_list[1][1])/2]
middle23=[(coor_list[1][0]+coor_list[2][0])/2,(coor_list[1][1]+coor_list[2][1])/2]
middle34=[(coor_list[2][0]+coor_list[3][0])/2,(coor_list[2][1]+coor_list[3][1])/2]
#middle41=[(coor_list[3][0]+coor_list[0][0])/2,(coor_list[3][1]+coor_list[0][1])/2]
area_quad=abs(((middle12[0]*middle23[1])+(middle23[0]*middle34[1])+(middle34[0]*middle12[1]))-((middle12[1]*middle23[0])+(middle23[1]*middle34[0])+(middle34[1]*middle12[0])))*2

#print(area_quad)a

#detect the min x and min_index
if coor_list[0][0]<coor_list[1][0] and coor_list[0][0]<coor_list[2][0] and coor_list[0][0]<coor_list[3][0]:
    x_min=coor_list[0]
    x_min_index=0
elif coor_list[1][0]<coor_list[0][0] and coor_list[1][0]<coor_list[2][0] and coor_list[1][0]<coor_list[3][0]:
    x_min=coor_list[1]
    x_min_index=1
elif coor_list[2][0]<coor_list[0][0] and coor_list[2][0]<coor_list[1][0] and coor_list[2][0]<coor_list[3][0]:
    x_min=coor_list[2]
    x_min_index=2
else:
    x_min=coor_list[3]
    x_min_index=3

#detect the max x
if coor_list[0][0]>coor_list[1][0] and coor_list[0][0]>coor_list[2][0] and coor_list[0][0]>coor_list[3][0]:
    x_max=coor_list[0]
    x_max_index=0
elif coor_list[1][0]>coor_list[0][0] and coor_list[1][0]>coor_list[2][0] and coor_list[1][0]>coor_list[3][0]:
    x_max=coor_list[1]
    x_max_index=1
elif coor_list[2][0]>coor_list[0][0] and coor_list[2][0]>coor_list[1][0] and coor_list[2][0]>coor_list[3][0]:
    x_max=coor_list[2]
    x_max_index=2
else:
    x_max=coor_list[3]
    x_max_index=3

"""
from operator import itemgetter
x_min=min(coor_list,key=itemgetter(0))
print(x_min)
x_max=max(coor_list,key=itemgetter(0))     # if we cannot use any library
print(x_max)
y_min=min(coor_list,key=itemgetter(1))
print(y_min)
y_max=max(coor_list,key=itemgetter(1))
print(y_max)"""

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


indexs=[0,1,2,3]
indexs.pop(x_max_index)
indexs.pop(x_min_index)

#equation of the line
m=(x_max[1]-x_min[1])/(x_max[0]-x_min[0])
#if coor_list[indexs[0]][1]-coor_list[x_max_index][1]>m(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and coor_list[indexs[1]][1]-coor_list[x_max_index][1]>m(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):



if coor_list[indexs[0]][1]>coor_list[x_max_index][1] and coor_list[indexs[0]][1]>coor_list[x_min_index][1] and coor_list[indexs[1]][1]>coor_list[x_max_index][1] and coor_list[indexs[1]][1]>coor_list[x_min_index][1]:
    bottom_area=(abs(coor_list[x_max_index][1])+abs(coor_list[x_min_index][1]))*(coor_list[x_max_index][0]-coor_list[x_min_index][0])/2
    if abs(x_max_index-x_min_index)!=1 or abs(x_max_index-x_min_index)!=3:
        if coor_list[indexs[0]][1]<coor_list[indexs[1]][1]:
            bottom_point=coor_list[indexs[0]]
        else:
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))*2
        bottom_area+=triangle
    print(bottom_area)    
elif coor_list[indexs[0]][1]<coor_list[x_max_index][1] and coor_list[indexs[0]][1]<coor_list[x_min_index][1] and coor_list[indexs[1]][1]<coor_list[x_max_index][1] and coor_list[indexs[1]][1]<coor_list[x_min_index][1]:
    bottom_area=(abs(coor_list[x_max_index][1])+abs(coor_list[x_min_index][1]))*(coor_list[x_max_index][0]-coor_list[x_min_index][0])/2
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if coor_list[indexs[0]][1]>coor_list[indexs[1]][1]:
            bottom_point=coor_list[indexs[0]]
        else:
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))*2
        bottom_area-=triangle
    print(bottom_area-area_quad)
    


else:
    pass








"""
if abs(x_max_index-x_min_index)==3:

if abs(x_max_index-x_min_index)==2:

if abs(x_max_index-x_min_index)==1:    
"""
