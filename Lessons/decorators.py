def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

# wrapping hello function with announce decorator function ex: for a web app, if you want a function to run only if the user
# logs in, you can write a function to check if the user is logged in and add it as a decorator to only functions
@announce
def hello():
    print("Hello, world!")

hello()