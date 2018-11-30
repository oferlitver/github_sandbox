import os
import numpy as np

# this is a new comment
def main():
    print os.getcwd()
    mat = np.array([[1, 2],
                    [3, 4]])
    print mat.transpose()

if __name__ == '__main__':
    main()
