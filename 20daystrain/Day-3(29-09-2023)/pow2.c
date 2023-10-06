//determine a number is power of 2 or not
#include<stdio.h>
main()
{
	int n,c=0,i=0;
	printf("Enter number:");
	scanf("%d",&n);
	/*while(n),c=0
	{
	   c++;
	   n=n&(n-1);	
	}*/
	while(n)
	{
		if(2<<i==n)
		{
			break;
		}
		else if(2<<i>n)
		{
			c++;
			break;
		}
		i++;
	}
	if(c==1)
	printf("Not a power of 2");
	else
	printf("power of 2");
}

