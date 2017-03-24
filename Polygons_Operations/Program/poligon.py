from PolygonArea import get_polygon_area
from PolygonArea import get_length

def create_polygon(puncte,filename):
    with open(filename,'r') as f:
        for line in f:
            line = tuple(map(float,line.split()))
            if line:
                puncte.append(line)


def print_poligon(puncte):
    for i in range(len(puncte)):
        print(puncte[i])


def get_rectangle(puncte):
    xmin = min([ x[0] for x in puncte])
    ymin = min([ x[1] for x in puncte])
    xmax = max([ x[0] for x in puncte])
    ymax = max([x[1] for x in puncte])
    print("The  rectangle that covers the polygon has these coordinates")
    print("A(", xmin, ',', ymin, ')')
    print("B(", xmax, ',', ymin, ')')
    print("C(", xmax, ',', ymax, ')')
    print("D(", xmin, ',', ymax, ')')

def get_perimeter(puncte):
    perimetru = []
    n = len(puncte)
    for i in range(n):
        if i!=n-1:
            punct1 = [x for x in puncte[i]]
            punct2 = [x for x in puncte[i + 1]]
            perimetru.append(get_length(punct1[0],punct1[1],punct2[0],punct2[1]))
        else:
            punct1 = [x for x in puncte[i]]
            punct2 = [x for x in puncte[0]]
            perimetru.append(get_length(punct1[0], punct1[1], punct2[0], punct2[1]))
    return sum(perimetru)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def IsConvex(puncte):
    n = len(puncte)
    if n<4:
        return 1
    is_negative = 0
    is_positive = 0
    for A in range(n):
        B = (A+1) % n
        C = (B+1) % n
        punct1 = [x for x in puncte[A]]
        punct2 = [x for x in puncte[B]]
        punct3 = [x for x in puncte[C]]

        cross_product = cross(punct1,punct2,punct3)
        if cross_product < 0:
            is_negative = 1
        else:
            is_positive = 1

        if is_negative and is_positive:
            return 0
    return 1


def concatenate(polygon1, polygon2):
    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = polygon1 + polygon2
    points = sorted(set(points))

    if len(points) <= 1:
        return points
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    return lower[:-1] + upper[:-1]

def compare_polygons(first,second):
    if get_polygon_area(first) < get_polygon_area(second):
        print("Second polygon is bigger")
    else:
        print("First polygon is bigger")


