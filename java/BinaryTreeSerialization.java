import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class BinaryTreeSerialization {
  static class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
      this.val = val;
    }
  }

  public static List<Integer> serialize(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    serialize(root, result);
    return result;
  }

  private static void serialize(TreeNode root, List<Integer> result) {
    if (root == null)
      result.add(null);
    else {
      result.add(root.val);
      serialize(root.left, result);
      serialize(root.right, result);
    }
  }

  public static TreeNode deserialize(List<Integer> tree) {
    if (tree == null || tree.isEmpty())
      throw new IllegalArgumentException();

    if (tree.get(0) == null)
      return null;

    Stack<Object[]> stack = new Stack<Object[]>();

    TreeNode root = null;
    for (Integer val : tree) {
      if (val != null) {
        TreeNode cur = new TreeNode(val);
        if (stack.isEmpty()) {
          root = cur;
        } else if ((boolean) stack.peek()[1]) {
          ((TreeNode) stack.peek()[0]).right = cur;
        } else {
          ((TreeNode) stack.peek()[0]).left = cur;
        }
        stack.push(new Object[] { cur, false });
      } else {
        while (!stack.isEmpty() && (boolean) stack.peek()[1])
          stack.pop();
        if (!stack.isEmpty())
          stack.peek()[1] = true;
      }
    }

    return root;
  }

  public static void main(String[] args) {
    Integer[] arr = new Integer[] {30, 10, 50, null, null, null, 20, 45, null, null, 35, null, null};
    List<Integer> serialized = Arrays.asList(arr);
    
    TreeNode root = deserialize(serialized);
    List<Integer> reseralized = serialize(root);

    for (Integer i : reseralized)
    {
      if (i != null)
        System.out.print(i);
      else
        System.out.print('#');
      
      System.out.print(' ');
    }
  }
}
