from src.services.priority_queue import sort_priority


def update_pkg_pool(packages, update_time, package_history):
    print('Initializing empty package pool...')
    print("Update time: ", update_time.strftime('%I:%M %p'))
    pkg_pool = []

    print('Adding eligible packages to the package pool...')
    for package in packages:
        if package.available_time <= update_time and package not in package_history:
            # print(f'Adding {package} to the pool...')
            pkg_pool.append(package)

    print('Sorting package pool by priority...')
    pkg_pool = sort_priority(pkg_pool)

    print('Package pool update complete')
    return pkg_pool, package_history
