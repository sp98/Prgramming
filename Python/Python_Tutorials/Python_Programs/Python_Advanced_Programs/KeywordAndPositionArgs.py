def method1(arg1, arg2, arg3=3, arg4='four'):
    # two positional arguments (Default), 2 keyword arguments(non defualt)
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

if __name__ == '__main__':
    method1(1, 2, arg4=4);
