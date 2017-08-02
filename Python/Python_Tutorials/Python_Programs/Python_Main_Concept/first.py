
print("This is first and will always be run as we are import first into second")
if __name__ == "__main__":
    print("Now first is {}".format(__name__))
else:
    print("First is not main now", __name__)
    