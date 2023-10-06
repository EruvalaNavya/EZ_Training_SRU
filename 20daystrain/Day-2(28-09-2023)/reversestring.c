#include<stdio.h>
#include<String.h>
int main()
{
	char str[50],str1[50];
	int i=0,j=0;
	gets(str);
	int len=strlen(str);
    for(i=len-1;i>=0;i--)
    {
    	str1[j]=str[i];
    	j++;
	}
	i=0,j=0;
	for(i=0;i<len;i++)
	{
		if(str[i]==' ')
		printf(" ");
		else if(str[i]>='a'&&str[i]<='z')
		{
			for(j=0;j<len;j++)
			{
				if(str1[j]==' ')
				continue;
				else if(str[j]>='a'&&str[j]<='z')
				printf("%c",str1[j]);
				else
				continue;
			}
		}
		else
		{
			printf("%c",str[i]);
		}
	}
}

