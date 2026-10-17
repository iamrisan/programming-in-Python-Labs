# Lab 05 - Exercise 1: Campus Resource Tracker
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2],
]


def display_resources(resources):
    if not resources:
        print("No resources found.")
        return
    for resource in resources:
        resource_id, name, category, quantity = resource
        if quantity < 0:
            print(f"Invalid quantity for {name}: {quantity}")
        else:
            print(f"ID: {resource_id}, Name: {name}, Category: {category}, Quantity: {quantity}")


def search_by_category(resources, category):
    matches = [r for r in resources if r[2].lower() == category.lower()]
    if not matches:
        print("No resources found in this category.")
    else:
        display_resources(matches)


def find_unavailable(resources):
    unavailable = [r for r in resources if r[3] == 0]
    if not unavailable:
        print("No unavailable resources.")
    else:
        display_resources(unavailable)


def search_by_id(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            display_resources([resource])
            return
    print("Unknown resource ID.")


if __name__ == "__main__":
    print("All resources:")
    display_resources(resources)
    print("\nElectronics:")
    search_by_category(resources, "Electronics")
    print("\nUnavailable resources:")
    find_unavailable(resources)
    print("\nTest: unknown ID")
    search_by_id(resources, 999)
    print("\nTest: negative quantity")
    display_resources([[106, "Printer", "Electronics", -2]])
    print("\nTest: empty list")
    display_resources([])
