import java.util.HashMap;

class Point {
  int x;
  int y;

  Point() {
    x = 0;
    y = 0;
  }

  Point(int a, int b) {
    x = a;
    y = b;
  }
}

class HashablePoint extends Point {
  @Override
  public int hashCode()
  {
    return x ^ y;
  }
  
  @Override
  public boolean equals(Object o)
  {
    if (!(o instanceof HashablePoint))
      return false;
    
    HashablePoint p = (HashablePoint) o;
    return x == p.x && y == p.y;
  }
  
  HashablePoint(Point p)
  {
    x = p.x;
    y = p.y;
  }
}

public class MaxPointsOnLine {
  public int maxPoints(Point[] points) {
    // IMPORTANT: Please reset any member data you declared, as
    // the same Solution instance will be reused for each test case.
    HashMap<HashablePoint, Integer> map = new HashMap<HashablePoint, Integer>();
    for (Point p : points)
    {
      HashablePoint hp = new HashablePoint(p);
      if (map.containsKey(hp))
        map.put(hp, map.get(hp) + 1);
      else
        map.put(hp, 1);
    }
    
    int max = Math.min(points.length, 2);

    for (HashablePoint p1 : map.keySet()) {
      max = Math.max(max, map.get(p1));
      for (HashablePoint p2 : map.keySet()) {
        if (p1.equals(p2))
          continue;
        
        int count = map.get(p1) + map.get(p2);
        for (HashablePoint p3 : map.keySet()) {
          if (p1.equals(p3) || p2.equals(p3))
            continue;
          
          if (onSameLine(p1, p2, p3))
            count += map.get(p3);
        }
        max = Math.max(count, max);
      }
    }

    return max;
  }

  private boolean onSameLine(Point p1, Point p2, Point p3) {
    int a = (p3.x - p1.x) * (p2.y - p1.y);
    int b = (p2.x - p1.x) * (p3.y - p1.y);
    return a == b;
  }

  public static void main(String[] args) {
    System.out.println(new MaxPointsOnLine().maxPoints(new Point[] {
        new Point(0, 0), new Point(1, 1), new Point(1, -1) }));
  }
}
