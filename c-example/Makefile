
all: Test.o LinkedList.o
	gcc Test.o LinkedList.o -o main

Test.o: Test.c
	gcc -c Test.c


LinkedList.o: LinkedList.c List.h
	gcc -c LinkedList.c


clean:
	rm *.o main


