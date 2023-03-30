package main.java.mylib.datastructures.linear;

public class SLL {

    // - 2 constructors:
    // o Default constructor with no arguments that creates a null head object
    // o Overload constructor with a Node object argument to use as head
    // o You may combine both using default arguments if you prefer to

    // - InsertHead(node)
    // o Inserts node object at head of the list
    // - InsertTail(node)
    // o Inserts node object at the tail of the list
    // - Insert(node,position)
    // o Inserts node object in the specified position
    // ▪ Ex. Insert(node ,5) → inserts node to 5th position in list
    // - SortedInsert(node)
    // o Inserts node object in its proper position in a sorted list
    // o Must check for list sort validity
    // ▪ If list is found to be out of order, it must call the sort function first
    // before
    // inserting
    // ▪ Note that you should only execute sort if the list is found to be out of
    // order
    // to avoid slowing down the insertion by executing sorting every time you
    // insert
    // ▪ Might need to implement a helper function isSorted(), or find a creative
    // way to know if the list is sorted
    // - Search(node)
    // o Looks up node in the list
    // ▪ If found it returns the object
    // ▪ Otherwise returns null
    // - DeleteHead()
    // o Delete head node
    // - DeleteTail()
    // o Delete tail node
    // - Delete(node)
    // o Deletes the node if found in the list
    // - Sort()
    // o Applies insertion sort to the list
    // o The insertion part will start from the head unlike the usual insertion sort
    // algorithm
    // ▪ Instead of tracking back the list
    // o Note that the sort method and SortedInsert can use each other to
    // efficiently
    // reduce code redundancy (not mandatory)
    // - Clear()
    // o Deletes the whole list
    // - Print()
    // o Prints the list information on the screen, this includes
    // ▪ List length
    // ▪ Sorted status
    // ▪ List content
    // ▪ Make sure to show information with relevant print statements to be
    // readable by the user

}