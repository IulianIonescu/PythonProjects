import math
def get_length(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def get_triangle_area(x0,y0,x1,y1,x2,y2):
    a = get_length(x0,y0,x1,y1)
    b = get_length(x1, y1, x2, y2)
    c = get_length(x0, y0, x2, y2)
    p = (a + b + c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def get_center_of_gravity(puncte):
    n = len(puncte)
    x = (sum([ x[0] for x in puncte])/n)
    y =(sum([ x[1] for x in puncte])/n)
    return (x,y)

def get_polygon_area(puncte):
    n = len(puncte)
    G = get_center_of_gravity(puncte)
    polygon_area = 0
    for i in range(0,n):
        if i!=n-1:
            punct1 = [x for x in puncte[i]]
            punct2 = [x for x in puncte[i + 1]]
            polygon_area = polygon_area + get_triangle_area(G[0],G[1],punct1[0],punct1[1],punct2[0],punct2[1])
        else:
            punct1 = [x for x in puncte[i]]
            punct2 = [x for x in puncte[0]]
            polygon_area = polygon_area + get_triangle_area(G[1], G[1], punct1[0],punct1[1], punct2[0], punct2[1])
    return polygon_area