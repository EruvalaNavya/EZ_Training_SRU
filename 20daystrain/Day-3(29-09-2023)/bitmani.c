//set ith bit 1 0r not,ith bit from right
#include<stdio.h>
int main()
{
	long long int a;
	int i,b;
	printf("Enter number:");
	scanf("%lld",&a);
	printf("\nEnter position to set:");
	scanf("%d",&i);
	if(a&1<<(i-1))
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
}
