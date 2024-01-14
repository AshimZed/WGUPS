
def update_links(package_list):
    package_dict = {package.package_id: package for package in package_list}
    change_flag = True

    while change_flag:
        change_flag = False

        # Ensure mutual linking
        for package in package_list:
            for lpkg_id in package.linked_packages:
                if lpkg_id in package_dict and package.package_id not in package_dict[lpkg_id].linked_packages:
                    package_dict[lpkg_id].linked_packages.add(package.package_id)
                    change_flag = True

        # Update links for indirectly linked packages
        for package in package_list:
            all_linked_packages = set()
            for lpkg_id in package.linked_packages:
                all_linked_packages.update(package_dict[lpkg_id].linked_packages)

            # Remove the package itself from the set of linked packages
            all_linked_packages.discard(package.package_id)

            # Update the package's linked packages
            package.linked_packages.update(all_linked_packages)
