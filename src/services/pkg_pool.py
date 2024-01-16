from src.datatypes.status import Status
from src.services.priority_queue import sort_priority
from src.utils.check_log import log_exists
from src.utils.log_event import log_package_event


def update_pkg_pool(log_file, packages, update_time, package_history):
    # print('Initializing empty package pool...')
    # print("Update time: ", update_time.strftime('%I:%M %p'))
    pkg_pool = []

    # print('Adding eligible packages to the package pool...')
    for package in packages:
        if package.available_time <= update_time and package not in package_history:
            # print(f'Adding {package} to the pool...')
            pkg_pool.append(package)
            if not log_exists(log_file, package, Status.AT_DEPOT):
                log_package_event(log_file, update_time, package, Status.AT_DEPOT)

    # print('Sorting package pool by priority...')
    pkg_pool = sort_priority(pkg_pool)

    # print('Package pool update complete')
    return pkg_pool, package_history
