//determine a number is power of 2 or not,4 or not
#include<stdio.h>
int main()
{
	int n,i=1,c=0;
	printf("Enter number:");
	scanf("%d",&n);
	while(n)
	{
	   if(4<<i==n)
	    {
	    	break;
		}
		else if(4<<i>n)
		{
			c++;
		}
		i++;	
	}
	if(c>=1)
	printf("Not a power of 4");
	else
	printf("%d is a power of 4",n);
}

