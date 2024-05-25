class Route:
    
    # Route constructor

    def __init__(Self, path, rhandler):
        Self.path = path
        Self.rhandler = rhandler
        # automatically set the left and right children to NULL, as these are null by default they are not needed in the constructor
        Self.left = None
        Self.right = None

    # Get left

    def get_left():
        return Self.left
    
    # Get right
    
    def get_right():
        return Self.right
    
    
    def add_route(root, path, rhandler):

        # Let's check if the route exists
        if (root == None):
            # Create new Route.
            root = Route(path, rhandler)
            return

        if (strcmp(path, root.path) > 0):
            # Add the left child route
            add_route(root.left, path, rhandler)

        else:
            # Otherwise, add the right child route.
            add_route(root.right, path, rhandler)

    
    # Routing methods

    def index(Socket client):
        # Empty method for now
    
    def about(Socket client):
        # Empty method for now
