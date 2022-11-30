coor_list=eval(input())#take the input as a list
#find the middle points of the first three edges
middle12=[(coor_list[0][0]+coor_list[1][0])/2,(coor_list[0][1]+coor_list[1][1])/2]
middle23=[(coor_list[1][0]+coor_list[2][0])/2,(coor_list[1][1]+coor_list[2][1])/2]
middle34=[(coor_list[2][0]+coor_list[3][0])/2,(coor_list[2][1]+coor_list[3][1])/2]
#calculate area of quad by using area of traingle which points' are what we found
area_quad=abs(((middle12[0]*middle23[1])+(middle23[0]*middle34[1])+(middle34[0]*middle12[1]))-((middle12[1]*middle23[0])+(middle23[1]*middle34[0])+(middle34[1]*middle12[0])))*2
max_list,min_list=[],[]
#find minimun value(s) of x 
if coor_list[0][0]<=coor_list[1][0] and coor_list[0][0]<=coor_list[2][0] and coor_list[0][0]<=coor_list[3][0]:
    min_list.append(0)
if coor_list[1][0]<=coor_list[0][0] and coor_list[1][0]<=coor_list[2][0] and coor_list[1][0]<=coor_list[3][0]:
    min_list.append(1)
if coor_list[2][0]<=coor_list[0][0] and coor_list[2][0]<=coor_list[1][0] and coor_list[2][0]<=coor_list[3][0]:
    min_list.append(2)
if coor_list[3][0]<=coor_list[0][0] and coor_list[3][0]<=coor_list[1][0] and coor_list[3][0]<=coor_list[2][0]:
    min_list.append(3)
#station in which there are more than one point whose x values are same, to choose a x_min point compare y values.
if len(min_list)==2 and abs(coor_list[min_list[0]][1])>abs(coor_list[min_list[1]][1]):
    x_min_index=min_list[1]
else:
    x_min_index=min_list[0]
#find maximum value(s) of x
if coor_list[0][0]>=coor_list[1][0] and coor_list[0][0]>=coor_list[2][0] and coor_list[0][0]>=coor_list[3][0]:
    max_list.append(0)
if coor_list[1][0]>=coor_list[0][0] and coor_list[1][0]>=coor_list[2][0] and coor_list[1][0]>=coor_list[3][0]:
    max_list.append(1)
if coor_list[2][0]>=coor_list[0][0] and coor_list[2][0]>=coor_list[1][0] and coor_list[2][0]>=coor_list[3][0]:
    max_list.append(2)
if coor_list[3][0]>=coor_list[0][0] and coor_list[3][0]>=coor_list[1][0] and coor_list[3][0]>=coor_list[2][0]:
    max_list.append(3)
#station in which there are more than one point whose x values are same, to choose a x_max point compare y values.
if len(max_list)==2 and abs(coor_list[max_list[0]][1])>abs(coor_list[max_list[1]][1]):
    x_max_index=max_list[1]
else:
    x_max_index=max_list[0]
# find the indexes of other points
indexs=[0,1,2,3]
indexs.remove(x_max_index) 
indexs.remove(x_min_index)
#slope of (m_min,m_max)line & equation of the line
m=(abs(coor_list[x_max_index][1])-abs(coor_list[x_min_index][1]))/(coor_list[x_max_index][0]-coor_list[x_min_index][0])
bottom_area=(abs(coor_list[x_max_index][1])+abs(coor_list[x_min_index][1]))*abs(coor_list[x_max_index][0]-coor_list[x_min_index][0])/2
#both "other points" higher than line
if abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])>m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if abs(abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])-(m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0])))/(1+m**2)**(1/2)<abs(abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])-(m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0])))/(1+m**2)**(1/2):
            bottom_point=coor_list[indexs[0]]
        else:
            
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area+=triangle
    print("%.2f"%bottom_area)    

#both "other points" lower than line
elif abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0]) and abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1])<m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0]):
    if abs(x_max_index-x_min_index)!=1 and abs(x_max_index-x_min_index)!=3:
        if abs(coor_list[indexs[0]][1])>abs(coor_list[indexs[1]][1]):
            bottom_point=coor_list[indexs[0]]
        else:
            bottom_point=coor_list[indexs[1]]
        triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
        bottom_area-=triangle
    print("%.2f"%(bottom_area-area_quad))
#else, this quad is a convex!!     
else: #Find the point which is closer
    if m*(coor_list[indexs[1]][0]-coor_list[x_max_index][0])-(abs(coor_list[indexs[1]][1])-abs(coor_list[x_max_index][1]))>m*(coor_list[indexs[0]][0]-coor_list[x_max_index][0])-(abs(coor_list[indexs[0]][1])-abs(coor_list[x_max_index][1])):
        bottom_point=coor_list[indexs[1]]
    else:
        bottom_point=coor_list[indexs[0]]
    # find the are of (m_min,m_max,closer_point)triangle   
    triangle=abs(((coor_list[x_max_index][0]*coor_list[x_min_index][1])+(coor_list[x_min_index][0]*bottom_point[1])+(bottom_point[0]*coor_list[x_max_index][1]))-((coor_list[x_max_index][1]*coor_list[x_min_index][0])+(coor_list[x_min_index][1]*bottom_point[0])+(bottom_point[1]*coor_list[x_max_index][0])))/2
    bottom_area-=triangle
    print("%.2f"%bottom_area)