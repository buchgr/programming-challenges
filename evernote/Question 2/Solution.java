import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;

public class Solution
{
	static class FrequencyCounter
	{
		Map<String, Integer> freqdist;
		FrequencyCounter(int initialCapacity)
		{
			if (initialCapacity <= 0)
				throw new IllegalArgumentException("initialCapacity <= 0");
			
			freqdist = new HashMap<>(initialCapacity);
		}
		
		void count(String word)
		{
			Integer oldVal = freqdist.get(word);
			if (oldVal == null)
				oldVal = 0;
			
			freqdist.put(word, oldVal+1);
		}
		
		void printMostFrequent(int k)
		{
			if (k < 0)
				throw new IllegalArgumentException("k < 0");
			
			if (k == 0)
				return;
			
			final class FrequencyComparator implements Comparator<Entry<String, Integer>>
			{
				@Override
				public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
					// ascending order
					int res = o1.getValue() - o2.getValue();
					if (res == 0)
						// inverse lexicographical order, so that lexicographically bigger
						// values are removed first from the pq
						res = o2.getKey().compareTo(o1.getKey());
					return res;
				}
			}
			
			PriorityQueue<Entry<String, Integer>> pq;
			Iterator<Entry<String, Integer>> iter;
			
			pq = new PriorityQueue<>(k, new FrequencyComparator());
			iter = freqdist.entrySet().iterator();
			while (iter.hasNext())
			{
				pq.add(iter.next());
				if (pq.size() > k)
					pq.poll();
			}
			
			List<String> buffer = new ArrayList<>(pq.size());
			while (!pq.isEmpty())
				buffer.add(pq.poll().getKey());
			
			// output is sometimes a performance bottleneck with interviewstreet
			// so to make sure buffer the output first
			StringBuilder ioBuf = new StringBuilder();
			for (int i = buffer.size()-1; i >= 0; i--)
				ioBuf.append(buffer.get(i))
				     .append(System.lineSeparator());
			System.out.print(ioBuf);
		}
	}
	
	
	public static void main(String... args) throws IOException
	{
		try(BufferedReader reader = new BufferedReader(new InputStreamReader(System.in)))
		{
			int N = Integer.parseInt(reader.readLine());
			FrequencyCounter counter = new FrequencyCounter(N);
			
			while (N-- > 0)
				counter.count(reader.readLine());
			
			int k = Integer.parseInt(reader.readLine());
			counter.printMostFrequent(k);
		}
	}
}