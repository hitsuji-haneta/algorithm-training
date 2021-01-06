import os


def search(dir, name):
    queue = [dir]

    while len(queue) > 0:
        dir = queue.pop()
        for i in os.listdir(dir):
            if i == name:
                print(dir + i)
            if os.path.isdir(dir + i):
                if os.access(dir + i, os.R_OK):
                    queue.append(dir + i + '/')


search('../', 'pyvenv.cfg')
