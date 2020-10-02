#include <iostream>
#include <list>

using namespace std;

class HashTable{
private:
  list<int> *table;
  int total_elements;

  int getHash(int key){
    return key % total_elements;
  }

public:
  HashTable(int n){
    total_elements = n;
    table = new list<int>[total_elements];
  }

  void insertElement(int key){
    table[getHash(key)].push_back(key);
  }

  void removeElement(int key){
    int x = getHash(key);

    list<int>::iterator i; 
    for (i = table[x].begin(); i != table[x].end(); i++) { 
      // Check if the iterator points to the required item:
      if (*i == key) 
        break;
    }

    if (i != table[x].end()) 
      table[x].erase(i);
  }
};
