from src.services.priority_queue import sort_priority


def update_pkg_pool(packages, update_time):
    pkg_pool = []
    for package in packages:
        if package.available_time <= update_time:
            pkg_pool.append(package)
    pkg_pool = sort_priority(pkg_pool)
    return pkg_pool
