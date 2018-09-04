#include "List.h"
#include <stdlib.h>


struct list *newList(void){
    struct list *new = malloc(sizeof(struct list));
    new->head = NULL;
    new->size = 0;
    return new;
}

int add(struct list *l, int item){
    l->size++;
    struct node *newNode = malloc(sizeof(struct node));
    newNode->next = NULL;
    newNode->item = item;

    if (l->head == NULL){
        l->head = newNode;
    } else {
        struct node *current = l->head;
        while (current->next != NULL){
            current = current->next;
        }
        current->next = newNode;
    }
    return 0;
}

int size(struct list *l){
    return l->size;
}

int contains(struct list *l, int item){
    struct node *head = l->head;
    struct node *current = head;
    while (current != NULL){
        if (current->item == item) return 1;
        current = current->next;
    }
    return 0;
}

void print(struct list *l){

}