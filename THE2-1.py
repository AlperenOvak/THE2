coor_list=eval(input()) #take the input as a list
#find the middle points of tge first three edges
middle12=[(coor_list[0][0]+coor_list[1][0])/2,(coor_list[0][1]+coor_list[1][1])/2] 
middle23=[(coor_list[1][0]+coor_list[2][0])/2,(coor_list[1][1]+coor_list[2][1])/2]
middle34=[(coor_list[2][0]+coor_list[3][0])/2,(coor_list[2][1]+coor_list[3][1])/2]
#calculate area of quad by using area of traingle which points' are what we found
area_quad=abs(((middle12[0]*middle23[1])+(middle23[0]*middle34[1])+(middle34[0]*middle12[1]))-((middle12[1]*middle23[0])+(middle23[1]*middle34[0])+(middle34[1]*middle12[0])))*2

min_list=[]
max_list=[]
#detect the min x and min_index
if coor_list[0][0]<=coor_list[1][0] and coor_list[0][0]<=coor_list[2][0] and coor_list[0][0]<=coor_list[3][0]:
    min_list.append(coor_list[0])
    min_list.append(0)
if coor_list[1][0]<=coor_list[0][0] and coor_list[1][0]<=coor_list[2][0] and coor_list[1][0]<=coor_list[3][0]:
    min_list.append(coor_list[1])
    min_list.append(1)
if coor_list[2][0]<=coor_list[0][0] and coor_list[2][0]<=coor_list[1][0] and coor_list[2][0]<=coor_list[3][0]:
    min_list.append(coor_list[2])
    min_list.append(2)
if coor_list[3][0]<=coor_list[0][0] and coor_list[3][0]<=coor_list[1][0] and coor_list[3][0]<=coor_list[2][0]:
    min_list.append(coor_list[3])
    min_list.append(3)

if len(min_list)==4:
    if min_list[0][1]>min_list[2][1]:
        x_min=min_list[2]
        x_min_index=min_list[3]
    else:
        x_min=min_list[0]
        x_min_index=min_list[1]
else:
    x_min=min_list[0]
    x_min_index=min_list[1]
#detect the max x and index of max
if coor_list[0][0]>=coor_list[1][0] and coor_list[0][0]>=coor_list[2][0] and coor_list[0][0]>=coor_list[3][0]:
    max_list.append(coor_list[0])
    max_list.append(0)
if coor_list[1][0]>=coor_list[0][0] and coor_list[1][0]>=coor_list[2][0] and coor_list[1][0]>=coor_list[3][0]:
    max_list.append(coor_list[1])
    max_list.append(1)
if coor_list[2][0]>=coor_list[0][0] and coor_list[2][0]>=coor_list[1][0] and coor_list[2][0]>=coor_list[3][0]:
    max_list.append(coor_list[2])
    max_list.append(2)
if coor_list[3][0]>=coor_list[0][0] and coor_list[3][0]>=coor_list[1][0] and coor_list[3][0]>=coor_list[2][0]:
    max_list.append(coor_list[3])
    max_list.append(3)

if len(max_list)==4:
    if abs(max_list[0][1])>abs(max_list[2][1]):
        x_max=max_list[0]
        x_max_index=max_list[1]
    else:
        x_max=max_list[2]
        x_max_index=max_list[3]
else:
    x_max=max_list[0]
    x_max_index=max_list[1]

indexs=[0,1,2,3]  # find the other points' indexs
indexs.remove(x_max_index)
indexs.remove(x_min_index)

m=(abs(x_max[1])-abs(x_min[1]))/(x_max[0]-x_min[0]) #slope of (m_min,m_max)line
bottom_area=(abs(coor_list[x_max_index][1])+abs(coor_list[x_min_index][1]))*abs(coor_list[x_max_index][0]-coor_list[x_min_index][0])/2

#both points are higher than line
if abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if abs(coor_list[indexs[0]][1])<abs(coor_list[indexs[1]][1]):
            bottom_point=coor_list[indexs[0]]
        else:
            
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area+=triangle
    
    print("%.2f"%bottom_area)    

#both points are lower than line
elif abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if abs(coor_list[indexs[0]][1])>abs(coor_list[indexs[1]][1]):
            bottom_point=coor_list[indexs[0]]
        else:
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area-=triangle
    print("%.2f"%(bottom_area-area_quad))
    
else: #if nott this quad is a convex!! #Find the point which is closer
    if m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0])-(abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1]))>m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0])-(abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])):
        bottom_point=coor_list[indexs[1]]
    else:
        bottom_point=coor_list[indexs[0]]
    # find the are of (m_min,m_max,closer_point)triangle    
    triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
    bottom_area-=triangle
    print("%.2f"%bottom_area)