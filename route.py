from typing import Self
from strcmp import strcmp

class Route:
    
    # Route constructor

    def __init__(Self, path, rhandler):
        Self.path = path
        Self.rhandler = rhandler
        # automatically set the left and right children to NULL, as these are null by default they are not needed in the constructor
        Self.left = None
        Self.right = None

    @staticmethod
    def create_route(path, rhandler):
        return Route(path, rhandler)

    # Get left

    def get_left():
        return Self.left
    
    # Get right
    
    def get_right():
        return Self.right
    
    @staticmethod 
    def add_route(root, path, rhandler):

        # Let's check if the route exists
        if root is None:
            # Create new Route.
            return Route.create_route(path, rhandler)
        
        comparison = strcmp(path, root.path)

        if comparison < 0:
            if root.left is None:
                root.left = Route.create_route(path, rhandler)

            else:
                # Otherwise, add the right child route.
                Route.add_route(root.left, path, rhandler)

        else:
            if root.right is None:
                root.right = Route.create_route(path, rhandler)

            else:
                Route.add_route(root.right, path, rhandler)

        return root

    @staticmethod
    def find_route(root, path):
        # Check if the root exists.
        if root is None:
            return None
        
        comparison = strcmp(path, root.path)

        if comparison == 0:
            return root.rhandler
        elif comparison < 0:
            return Route.find_route(root.left, path)
        else:
            return Route.find_route(root.right, path)



