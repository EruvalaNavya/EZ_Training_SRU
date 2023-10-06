#include<stdio.h>
int main()
{
	int a,count=0;
	scanf("%d",&a);
	while(a)
	{
		count++;
		a=a&(a-1);
	}
	/*while(a>0)
	if(a&1)
	c++;
	a=a>>1;*/
	printf("Count set bits=%d",count);
}
