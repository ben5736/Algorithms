import java.util.ArrayList;
import java.util.TreeMap;

public class SubsetsII {
    public ArrayList<ArrayList<Integer>> subsetsWithDup(int[] num) {
        ArrayList<NumCount> numCount = count(num);
        return getSubsets(numCount);
    }
    
    private ArrayList<NumCount> count(int[] num) {
        TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
        ArrayList<NumCount> result = new ArrayList<NumCount>();
        
        for (int n : num)
        {
            if (map.containsKey(n))
                map.put(n, map.get(n) + 1);
            else
                map.put(n, 1);
        }
        
        for (int e : map.keySet())
            result.add(new NumCount(e, map.get(e)));
        
        return result;
    }
    
    private ArrayList<ArrayList<Integer>> getSubsets(ArrayList<NumCount> count) {
        return getSubsets(count, count.size());
    }
    
    private ArrayList<ArrayList<Integer>> getSubsets(ArrayList<NumCount> count, int n) {
        if (n == 0)
        {
            ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
            ArrayList<Integer> empty = new ArrayList<Integer>();
            result.add(empty);
            return result;
        }
        else
        {
            ArrayList<ArrayList<Integer>> result = getSubsets(count, n - 1);
            int size = result.size();
            for (int i = 1; i <= count.get(n - 1).count; i++)
            {
                for (int j = 0; j < size; j++)
                {
                    ArrayList<Integer> subset = new ArrayList<Integer>(result.get(j));
                    for (int k = 0; k < i; k++)
                        subset.add(count.get(n - 1).num);
                    result.add(subset);
                }
            }
            return result;
        }
    }
}

class NumCount {
    int num, count;
    
    NumCount(int n, int c) {
        num = n;
        count = c;
    }
}