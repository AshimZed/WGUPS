from src.datatypes.status import Status
from src.utils.log_event import log_package_event


def load_trucks(log_file, time, pkg_pool, package_history, trucks):
    truck_idx = 0
    full_trucks = set()
    change_flag = True

    while pkg_pool and change_flag:
        pkg_idx = 0
        change_flag = False
        current_truck = trucks[truck_idx]

        if len(full_trucks) == len(trucks):
            break

        if current_truck in full_trucks:
            truck_idx = (truck_idx + 1) % len(trucks)
            change_flag = True
            continue

        remaining_capacity = current_truck.max_inv - len(current_truck.inv)

        pkg = pkg_pool[pkg_idx]

        # Check if package is allowed on current truck
        while_counter = 0
        while current_truck.truck_id in pkg.banned_trucks:
            while_counter += 1
            pkg_idx += 1
            if pkg_idx >= len(pkg_pool):
                break
            pkg = pkg_pool[pkg_idx]
            if while_counter > len(pkg_pool):
                break

        if pkg.linked_packages:
            if len(pkg.linked_packages) <= remaining_capacity:
                for lpkg_id in pkg.linked_packages:
                    for lpkg in pkg_pool:
                        if lpkg.package_id == lpkg_id:
                            current_truck.inv.append(lpkg)
                            package_history.add(lpkg)
                            pkg_pool.remove(lpkg)
                            log_package_event(log_file, time, lpkg, Status.EN_ROUTE, current_truck)
                current_truck.inv.append(pkg)
                package_history.add(pkg)
                pkg_pool.remove(pkg)
                log_package_event(log_file, time, pkg, Status.EN_ROUTE, current_truck)
                change_flag = True
            else:
                truck_idx = (truck_idx + 1) % len(trucks)
                change_flag = True
                continue
        elif remaining_capacity > 0:
            current_truck.inv.append(pkg)
            package_history.add(pkg)
            pkg_pool.remove(pkg)
            log_package_event(log_file, time, pkg, Status.EN_ROUTE, current_truck)
            change_flag = True
        else:
            full_trucks.add(current_truck)
        truck_idx = (truck_idx + 1) % len(trucks)

    return pkg_pool, package_history, trucks
