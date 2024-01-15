from src.services.priority_queue import sort_priority


def update_pkg_pool(packages, update_time, package_history):
    pkg_pool = []
    for package in packages:
        if package.available_time <= update_time and package.package_id not in package_history:
            pkg_pool.append(package)
    pkg_pool = sort_priority(pkg_pool)
    return pkg_pool
