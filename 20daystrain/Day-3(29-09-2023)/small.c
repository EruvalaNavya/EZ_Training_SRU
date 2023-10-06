//smallest number greater than n with exactly 1 bit diff in binary form
#include<stdio.h>
int main()
{
	int a=15;//15=01111,16=10000 -->15 | 16 =31
	printf("%d",a | a+1);
}
