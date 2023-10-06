#include<stdio.h>
long long int fact(long long int n)
{
	if(n==0 || n==1)
	{
		return 1;
	}
	else
	{
		return n*fact(n-1);
	}
}
int main()
{
	long long int n;
	printf("Enter number:");
	scanf("%lld",&n);
	long long int val=fact(n);
	printf("\nFactorial of given number:%lld",val);
}
