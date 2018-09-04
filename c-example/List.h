
struct node {
    int item;
    struct node *next;
};

struct list {
    struct node *head;
    int size;
};

struct list *newList(void);
int add(struct list *l, int item);
int size(struct list *l);
int contains(struct list *l, int item);
void print(struct list *l);