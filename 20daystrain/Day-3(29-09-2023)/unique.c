//print lonely/unique integers in an array
#include<stdio.h>
main()
{
	int a,val=0,i=0;
	printf("Enter array size:");
	scanf("%d",&a);
	int ar[a];
	printf("\nEnter array elements:");
	for(i=0;i<a;i++)
	{
		scanf("%d",&ar[i]);
	}
	for(i=0;i<a;i++)
	{
		val=val^ar[i];
	}
	printf("%d",val);
}
