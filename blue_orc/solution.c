#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */    
	
	unsigned short r = 0;
	int instr = 0;
	char c[16];
	int quit = 0;
	
	while (!quit)
	{
		gets(c);
		
		instr = atoi(c);
		
		switch(instr)
		{
			case 0:
			{
				printf("%d\n", r);
				quit = 1;
				
				break;
			}
			
			case 1:
			{
				gets(c);
				r += atoi(c);
				
				break;
			}
			
			case 2:
			{
				gets(c);
				r -= atoi(c);
				
				break;
			}
			
			case 3:
			{
				gets(c);
				r *= atoi(c);
				
				break;
			}
		}
	}
	
	return 0;
}
