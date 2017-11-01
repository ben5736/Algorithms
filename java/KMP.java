
public class KMP {
	
	public static int find(String haystack, String needle)
	{
		if (haystack == null || needle == null)
			throw new IllegalArgumentException("Null parameter");
		
		if (haystack.length() < needle.length())
			return -1;
		
		int[] table = buildTable(needle);
		return match(haystack, needle, table);
	}
	
	private static int[] buildTable(String needle) {
		int[] table = new int[needle.length() + 1];
		
		int prefixTail = 0;
		for (int i = 2; i < table.length; i++)
		{
			while (prefixTail > 0 && needle.charAt(prefixTail) != needle.charAt(i - 1))
				prefixTail = table[prefixTail];
			
			if (needle.charAt(prefixTail) == needle.charAt(i - 1))
				prefixTail++;
			
			table[i] = prefixTail;
		}
		
		return table;
	}

	private static int match(String haystack, String needle, int[] table) {
		int matched = 0;
		
		for (int i = 0; i < haystack.length(); i++)
		{
			while (matched > 0 && haystack.charAt(i) != needle.charAt(matched))
				matched = table[matched];
			
			if (haystack.charAt(i) == needle.charAt(matched))
				matched++;
			
			if (matched == needle.length())
				return i - matched + 1;
		}
		
		return -1;
	}

	public static void main(String[] args)
	{
		System.out.println(find("abcde", ""));
	}
}
