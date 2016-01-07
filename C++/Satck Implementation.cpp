/*
 * Stack.cpp
 *
 *  Created on: Nov 29, 2015
 *      Author: Mj
 */
#include<iostream>
#include<conio.h>
using namespace std;

class node 	{
	node *next;
	int info;
	public:
		node()		{
			info = 0;
			next = NULL;
		}
		~node	()	{}
		void setValue(int value)	{
			info = value;
		}
		void setNext(node * abc)	{
			next = abc;
		}
		int getValue()	{
			return info;
		}
		node * getNext()	{
			return next;
		}
		
	
} *head;
bool push(int value)	{
	node *ptr = new node;
	if(!ptr)	{
		return false;
	}
	if(head == NULL)
		cout << "Creating stack\n";
	ptr->setValue(value);
	ptr->setNext(head);
	head = ptr;
	return true;
		}
bool pop()	{
	node *temp = new node;
	if(head == NULL)	{
		cout << "Stack empty already\n";
		return false;
	}
	temp = head;
	head = temp->getNext();
	cout << temp->getValue() << " removed\n";
	delete(temp);
	return true;
}
void disp()	{
	node *ptr = new node;
	ptr = head;
	while(ptr != NULL)	{
		cout << ptr->getValue() << ", ";
		ptr = ptr->getNext();
	}
	cout << endl;
}
int main()	{
	int val;
	int choice = 0;
	bool result;

	node *head = new node;
	while(choice != 4)	{
		cout << "Enter \n1. Push\n2. Pop\n3. Display\n4. Exit\n: ";
		cin >> choice;
		if(choice == 1)	{
			cout << "Enter data: ";
			cin >> val;
			result = push(val);
			if(result == true)	{
				cout << "Push Successful for value " << val << "\n";
			}
			else
				cout << "Push failed!\n";
		}
		if(choice == 2)	{
			result = pop();
			if(result == true)
				cout << "Pop operation successful\n";
			else
				cout << "Could not perform pop\n";
		}
		if(choice == 3)	{
			disp();
		}
		if(choice == 4)
			break;
		else
			cout << "Enter valid input\n";
	}
	return 0;
}

