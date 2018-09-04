#include "List.h"
#include "stdio.h"
#include "assert.h"

int main(int argc, char *argv){
    printf("testing Lists...\n");
    struct list *test1 = newList();
    assert(test1 != NULL);
    assert(test1->head == NULL);    
    assert(size(test1) == 0);
    printf("test1 passed\n");

    add(test1, 7);
    assert(size(test1) == 1);
    assert(contains(test1, 7) == 1);
    printf("test2 passed\n");

    add(test1, 8);
    add(test1, 9);
    
    assert(size(test1) == 3);
    assert(contains(test1, 8) == 1);
    assert(contains(test1, 9) == 1);
    assert(contains(test1, 10) == 0);

    printf("test3 passed\n");


}