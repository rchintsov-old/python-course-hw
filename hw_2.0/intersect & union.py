def intersect(*args):
    apd = set(args[0])
    for i in args[1:]:
        apd = apd.intersection(i)
    return apd

def union(*args):
    apd = set(args[0])
    for i in args[1:]:
        apd = apd.union(i)
    return apd

# -------------------
# non-hacking funcs
# -------------------

def intersect2(*args):
    apd = set(args[0])
    intersections = []
    for i in args[1:]:
        for j in i:
            if j in apd:
                intersections.append(j)
    return set(intersections)


def union2(*args):
    unions = []
    for i in args:
        unions += list(i)
    return set(unions)


def union3(*args):
    unions = set(args[0])
    for i in args[1:]:
        for j in i:
            if j not in unions:
                unions.add(j)
    return unions


# validating

# intersect([1,2,4], (2,5,6))
# intersect2([1,2,4,6], (2,5,6))
#
# union([1,2,4], (2,5,6,1))
# union2([1,2,4], (2,5,6,7))
# union3([1,2,4], (2,5,6,7))
#
# intersect2('abcd', 'achj')
#
# union('abcd', 'achj')
# union2('abcd', 'achj')
# union3('abcd', 'achj')
