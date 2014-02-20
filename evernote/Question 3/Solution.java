import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution
{
	public static void main(String... args) throws IOException
	{
		try(BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)))
		{
			int N = Integer.parseInt(reader.readLine());
			
			long[] nums = new long[N];
			for (int i=0; i < N; i++)
				nums[i] = Long.parseLong(reader.readLine());
			
			long totalProduct = 1;
			int zeros = 0;
			for (int i=0; i < N && zeros < 2; i++)
			{
				if (nums[i] == 0)
					zeros++;
				else
					totalProduct *= nums[i];
			}
			
			// output is sometimes a performance bottleneck with interviewstreet
			// so to make sure buffer the output first
			StringBuilder ioBuf = new StringBuilder();
			for (int i=0; i<N; i++)
			{
				if (zeros == 0)
					ioBuf.append(totalProduct / nums[i]);
				else if (zeros == 1)
					if (nums[i] == 0)
						ioBuf.append(totalProduct);
					else
						ioBuf.append("0");
				else
					ioBuf.append("0");
				ioBuf.append(System.lineSeparator());
			}

			System.out.print(ioBuf);
		}
	}
}