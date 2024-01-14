
def sort_priority(pkg_pool):
    a = []
    b = []
    for pkg in pkg_pool:
        if pkg.deadline:
            a.append(pkg)
        else:
            b.append(pkg)
    return a + b
