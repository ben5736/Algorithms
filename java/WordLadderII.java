import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

public class WordLadderII {
  
  public static void main(String[] args) {
    HashSet<String> set = new HashSet<String>();
    set.add("hot");
    //set.add("dot");
    set.add("dog");
    //set.add("lot");
    //set.add("log");
    for (ArrayList<String> path : new WordLadderII().findLadders("hot", "dog", set))
    {
      for (String word : path)
        System.out.format("%s ", word);
      System.out.println();
    }
  }
  public ArrayList<ArrayList<String>> findLadders(String start, String end,
      HashSet<String> dict) {
    dict.add(start);
    dict.add(end);

    HashMap<String, WordInfo> map = new HashMap<String, WordInfo>();
    LinkedList<String> queue = new LinkedList<String>();

    queue.add(start);
    map.put(start, new WordInfo(0));

    int minDist = -1;

    while (!queue.isEmpty()) {
      String cur = queue.remove();
      int curDist = map.get(cur).dist;

      if (minDist != -1 && curDist == minDist)
        break;

      char[] charArr = cur.toCharArray();

      for (int i = 0; i < charArr.length; i++) {
        char oldChar = charArr[i];
        for (char c = 'a'; c <= 'z'; c++) {
          charArr[i] = c;
          String potentialNeighbor = new String(charArr);

          if (dict.contains(potentialNeighbor)) {
            WordInfo neighborInfo = map.get(potentialNeighbor);
            if (neighborInfo == null) {
              neighborInfo = new WordInfo(curDist + 1);
              neighborInfo.parents.add(cur);
              map.put(potentialNeighbor, neighborInfo);
              queue.add(potentialNeighbor);
            } else if (neighborInfo.dist == curDist + 1) {
              neighborInfo.parents.add(cur);
            }

            if (potentialNeighbor.equals(end))
              minDist = curDist + 1;
          }
        }
        charArr[i] = oldChar;
      }
    }
    if (minDist == -1)
      return new ArrayList<ArrayList<String>>();
    return getPath(end, map);
  }

  private ArrayList<ArrayList<String>> getPath(String cur, HashMap<String, WordInfo> map) {
    ArrayList<String> parents = map.get(cur).parents;
    ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
    
    if (parents.isEmpty())
    {
      ArrayList<String> path = new ArrayList<String>();
      path.add(cur);
      result.add(path);
    }
    else
    {
      for (String parent : parents)
      {
        ArrayList<ArrayList<String>> subResults = getPath(parent, map);
        for (ArrayList<String> subResult : subResults)
          subResult.add(cur);
        result.addAll(subResults);
      }
    }
    
    return result;
  }

  class WordInfo {
    int dist;
    ArrayList<String> parents;

    public WordInfo(int d) {
      dist = d;
      parents = new ArrayList<String>();
    }
  }
}
