#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	int n, a[50], min, num, i, maxpos;
	cin >> n;
	for (i = 0; i < n; i++)	{
		scanf("%d", &a[i]);
	}
	
	int max = a[0];
	maxpos = 0;
	for (i =1; i < n; i++)	{
		if(max < a[i])	{
			max = a[i];
			maxpos = i;
		}
		
	}
	
	while (a[maxpos]!=0)	{
		min = a[maxpos];
		for (i = 0; i < n; i++)	{
			if(a[i] != 0 && a[i] < min)
				min = a[i];
		}
		num = 0;
		for ( i = 0; i < n; i++)	{
			if (a[i] != 0)	{
				a[i] -= min;
				num = num + 1;
			}
		}
		cout << num;
	}
	
	return 0;
}
