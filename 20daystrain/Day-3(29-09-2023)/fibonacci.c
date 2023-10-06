#include<stdio.h>
/*long long int fib(long long int n)
{
	long long int n1=0,n2=1;//takes long time duration
	if(n==0 || n==1)
	{
		return n;
	}
	else
	{
		return fib(n-1)+fib(n-2);
	}
}*/
int main()
{
	long long int n;
	printf("Enter number upto which you want to know fibonacci series:");
	scanf("%lld",&n);
	int i;
	long long int a=0,b=1,c;
	printf("%lld %lld ",a,b);
	for(i=2;i<n;i++)
	{
		c=a+b;
		printf("%lld ",c);
		a=b;
		b=c;
	}
}
