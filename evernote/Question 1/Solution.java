import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution
{
	static class CircularBuffer
	{
		private String[] buffer;
		private int head;
		private int tail;
		private int count;
		private boolean firstinsert;

		CircularBuffer(int N)
		{
			if (N < 0)
				throw new IllegalArgumentException("N < 0");

			buffer = new String[N];
			head = tail = count = 0;
			firstinsert = true;
		}

		void add(String s)
		{
			if (buffer.length == 0)
				return;

			if (!firstinsert)
			{
				tail = (tail+1) % buffer.length;
				if (head == tail)
					head = (head+1) % buffer.length;
			}
			else
				firstinsert = false;

			buffer[tail] = s;
			
			if (count < buffer.length)
				count++;
		}

		void removeFirst()
		{
			if (count > 0)
			{
				buffer[head] = null;
				count--;
				
				if (count == 0)
				{
					head = tail = 0;
					firstinsert = true;
				}
				else
					head = (head+1) % buffer.length;
			}
		}

		void list()
		{
			int i = head;
			// output is sometimes a performance bottleneck with interviewstreet
			// so to make sure buffer the output first
			StringBuilder ioBuf = new StringBuilder();
			while (i != tail)
			{
				ioBuf.append(buffer[i])
					 .append(System.lineSeparator());
				i = (i+1) % buffer.length;
			}

			if (count > 0)
				ioBuf.append(buffer[tail])
					 .append(System.lineSeparator());
			System.out.print(ioBuf);
		}
	}

	public static void main(String... args) throws IOException
	{
		try(BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)))
		{
			int N = Integer.parseInt(reader.readLine());
			CircularBuffer buf = new CircularBuffer(N);
			
			String command;
			while((command = reader.readLine()) != null && !command.equals("Q"))
			{
				if (command.equals("L"))
				{
					buf.list();
				}
				else if (command.startsWith("A"))
				{
					int n = Integer.parseInt(command.substring(2));
					while (n-- > 0)
						buf.add(reader.readLine());
				}
				else if (command.startsWith("R"))
				{
					int n = Integer.parseInt(command.substring(2));
					while (n-- > 0)
						buf.removeFirst();
				}
			}
		}
	}
}