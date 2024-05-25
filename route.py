class Route:
    
    # Route constructor

    def __init__(self, path, rhandler):
        self.path = path
        self.rhandler = rhandler
        # automatically set the left and right children to NULL, as these are null by default they are not needed in the constructor
        self.left = None
        self.right = None

    # Get left

    def get_left():
        return self.left
    
    # Get right
    
    def get_right():
        return self.right
    
    
    def add_route(root, path, rhandler): 
