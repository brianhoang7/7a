# Author: Brian Hoang
# Date: 11/13/2019
# Description: Function that takes list and modifies each object to its squared value

#takes mylist and modifies each object to be its squared value
def square_list(mylist):
    #to tally through the length of mylist
    tally = 0
    #multiplies each object by itself and replaces itself with the new value
    for tally in range(len(mylist)):
        mylist[tally] = mylist[tally] * mylist[tally]
        tally += 1



#num_list = [3, 4, 5, 6, 7]
#square_list(num_list)
#print(num_list)
