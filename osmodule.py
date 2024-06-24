import os
'''
os.makedirs("./tree/c/other_courses/cpp")
os.makedirs("./tree/c/other_courses/python")
os.makedirs("./tree/cpp/other_courses/c")
os.makedirs("./tree/cpp/other_courses/python")
os.makedirs("./tree/python/other_courses/c")
os.makedirs("./tree/python/other_courses/cpp")
'''


def find(path,dir):
    try:
        if os.path.exists(path):
            os.chdir(path)
        directories = os.listdir()
        for d in directories:
            find(d, dir)
        if os.path.basename(os.getcwd()) == dir:
            print(os.path.abspath(os.getcwd()))
        os.chdir("..")
    except Exception as e:
        print(e)

find("./tree/python", "python")