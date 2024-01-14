
def load_truck(pkg_pool, truck):
    while len(truck.inv) < truck.max_inv:
        if not pkg_pool:
            break
        pkg = pkg_pool.pop(0)
        truck.inv.append(pkg)
