
def update_pkg_pool(packages, update_time):
    pkg_pool = []
    for package in packages:
        if package.available_time <= update_time:
            pkg_pool.append(package)
    return pkg_pool
