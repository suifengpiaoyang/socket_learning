import sys

flag = sys.version_info[0]
if flag == 2:
    input = raw_input
elif flag == 3:
    input = input
else:
    print('This script is not suit for the system.')
    sys.exit()
