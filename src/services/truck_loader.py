
def load_trucks(pkg_pool, trucks):
    truck_idx = 0
    full_trucks = set()

    while pkg_pool:
        current_truck = trucks[truck_idx]

        if len(full_trucks) == len(trucks):
            break

        if current_truck in full_trucks:
            truck_idx = (truck_idx + 1) % len(trucks)
            continue

        remaining_capacity = current_truck.max_inv - len(current_truck.inv)

        pkg = pkg_pool[0]

        # Check if package is allowed on current truck
        if (truck_idx + 1) in pkg.banned_trucks:
            truck_idx = (truck_idx + 1) % len(trucks)
            continue

        if pkg.linked_packages:

            if len(pkg.linked_packages) <= remaining_capacity:
                for lpkg_id in pkg.linked_packages:
                    for lpkg in pkg_pool:
                        if lpkg.package_id == lpkg_id:
                            current_truck.inv.append(lpkg)
                            pkg_pool.remove(lpkg)
                current_truck.inv.append(pkg)
                pkg_pool.remove(pkg)
            else:
                truck_idx = (truck_idx + 1) % len(trucks)
                continue
        elif remaining_capacity > 0:
            current_truck.inv.append(pkg)
            pkg_pool.remove(pkg)
        else:
            full_trucks.add(current_truck)
        truck_idx = (truck_idx + 1) % len(trucks)
