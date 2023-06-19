# A decorator is a function that takes a function as input
# and returns a modified version of that function as output.

# You can imagine writing a decorator that checks if a user is login,
# and using that decorator on all of the functions that you want to make sure only work
# when a user is actually logged in.


def announce(f):
    """
    modifies another function by announcing that the function
    is about to run, and the function has completed running.
    
    Returns:

    wrapper(function)
    """
    def wrapper():
        """
        wraps function f with additional behavior
        """
        print("About to run a function...")
        f()
        print("Done with the function.")
    
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()