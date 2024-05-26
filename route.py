class Route:
    # Route constructor
    def __init__(self, path, rhandler):
        self.path = path
        self.rhandler = rhandler
        self.left = None
        self.right = None

    @staticmethod
    def create_route(path, rhandler):
        return Route(path, rhandler)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    @staticmethod 
    def add_route(root, path, rhandler):
        # Check if the root exists
        if root is None:
            # Create new Route
            return Route.create_route(path, rhandler)
        
        if path < root.path:
            if root.left is None:
                root.left = Route.create_route(path, rhandler)
            else:
                Route.add_route(root.left, path, rhandler)
        else:
            if root.right is None:
                root.right = Route.create_route(path, rhandler)
            else:
                Route.add_route(root.right, path, rhandler)

        return root

    @staticmethod
    def find_route(root, path):
        # Check if the root exists
        if root is None:
            return None
        
        if path == root.path:
            return root.rhandler
        elif path < root.path:
            return Route.find_route(root.left, path)
        else:
            return Route.find_route(root.right, path)
