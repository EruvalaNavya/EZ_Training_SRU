//determine a number is power of 4 or not
#include<stdio.h>
int main()
{
	int n,c=0,i=0;
	printf("Enter number:");
	scanf("%d",&n);
	while(n)
	{
		if(4<<(i*2)==n)
		{
			break;
		}
		else if(4<<(i*2)>n)
		{
			c++;
			break;
		}
		i++;
	}
	if(c==1)
	printf("Not a power of 4");
	else
	printf("power of 4");
}

