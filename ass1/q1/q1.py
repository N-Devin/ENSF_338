import sys

def do_stuff():
    if (len(sys.argv) < 2 or str.isdigit(sys.argv[1]) == False):
      print("Usage: python q1.py <list of numbers>")
      return
    int_list = [int(x) for x in sys.argv[1:]]
    int_list = [x*2 for x in int_list]
    int_list = int_list[::-1]  
    print(int_list)

if __name__ == '__main__':
    do_stuff()
