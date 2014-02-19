
public class MinimulWindowSubstring {
    public static String minWindow(String S, String T) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        if (S.equals("") || T.equals(""))
            return "";
        
        int[] tarMap = new int[256];
        for (int i = 0; i < T.length(); i++)
            tarMap[(int) T.charAt(i)]++;
            
        int[] map = new int[256];
        
        int lead = 0, trail = 0;
        int min = -1;
        int s = -1, e = -1;
        int count = 0;
        if (tarMap[(int) S.charAt(0)] > 0)
        {
            map[(int) S.charAt(0)]++;
            count++;
        }
        
        while (lead < S.length())
        {
            if (count == T.length()) {
                if (min == -1 || min > lead - trail + 1) {
                    min = lead - trail + 1;
                    s = trail;
                    e = lead;
                }
                
                char c = S.charAt(trail++);
                if (tarMap[(int) c] > 0)
                {
                    if (tarMap[(int) c] == map[(int) c])
                        count--;
                    map[(int) c]--;
                }
            }
            else
            {
                lead++;
                if (lead == S.length())
                    break;
                char c = S.charAt(lead);
                if (tarMap[(int) c] > 0)
                {
                    map[(int) c]++;
                        
                    if (map[(int) c] <= tarMap[(int) c])
                        count++;
                }
            }
        }
        
        return min == -1 ? "" : S.substring(s, e + 1);
    }
    
    public static void main(String[] args) {
    	System.out.println(minWindow("bdab", "ab"));
    }
}
