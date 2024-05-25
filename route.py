class Route:
    
    # Route constructor

    def __init__(Self, path, rhandler):
        Self.path = path
        Self.rhandler = rhandler
        # automatically set the left and right children to NULL, as these are null by default they are not needed in the constructor
        Self.left = None
        Self.right = None


    def create_route(path, rhandler):
        return Route(path, rhandler)
    # Get left

    def get_left():
        return Self.left
    
    # Get right
    
    def get_right():
        return Self.right
    
    
    def add_route(root, path, rhandler):

        # Let's check if the route exists
        if root is None:
            # Create new Route.
            return create_route(path, rhandler)
        
        comparison = strcmp(path, root.path)

        if comparison < 0:
            if root.left is None:
                root.left = create_route(path, rhandler)

            else:
                # Otherwise, add the right child route.
                add_route(root.left, path, rhandler)

        else:
            if root.right is None:
                root.right = create_route(path, rhandler)

            else:
                add_route(root.right, path, rhandler)

        return root

    # Routing methods

    def index(Socket client):
        # Empty method for now
    
    def about(Socket client):
        # Empty method for now
