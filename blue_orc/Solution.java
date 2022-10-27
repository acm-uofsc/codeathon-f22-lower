import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) {
		/* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
		Scanner sc = new Scanner(System.in);
		
		int r = 0;
		int instr = 0;
		boolean quit = false;
		
		while (!quit)
		{
			instr = Integer.parseInt(sc.nextLine());
			
			switch (instr)
			{
				case 0:
				{
					quit = true;
					
					break;
				}
				
				case 1:
				{
					r = (r + Integer.parseInt(sc.nextLine())) & 65535;
					
					break;
				}
				
				case 2:
				{
					r = (r - Integer.parseInt(sc.nextLine())) & 65535;
					
					break;
				}
				
				case 3:
				{
					r = (r * Integer.parseInt(sc.nextLine())) & 65535;
					
					break;
				}
			}
		}
		
		System.out.println(r);
	}
}