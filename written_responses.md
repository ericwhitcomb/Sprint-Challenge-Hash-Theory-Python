1. What is a regular expression and how does it work?

    Regular expressions are a set of syntax that helps find patterns in text.
    They allow you to create search patterns by unique, range, repeated, etc.
    Running regular expressions allows you to find patterns in text and some
    libraries allow you to update text.

2. What is an array and how does it work?

    An array is a block of memory of finite size used to hold repeated data of
    the same type. It allows memory to be incrementally accessed to step over
    each element for processing, searching, etc. It is a base data structure to 
    several higher level data structures, notably the hash table.

3. What is a hash table and how does it work?

    A hash table is a key/value pair data structure. Keys must be unique, values
    can be the same. Under the hood, it uses an array of a certain size to hold
    all the values. First, it uses a hash function to reduce the key/value down
    to an index within the range of the array. Since this can cause collisions
    due to different key/value pairs hashing down to the same index, a linked 
    list is used to store multiple pairs at that index. This structure allows for
    better insertion and retrieval, along with a linear, at worst, search.