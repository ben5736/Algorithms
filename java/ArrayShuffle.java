public class ArrayShuffle {
  /**
   * Move the element at start to end in place. Start must be after end.
   */
  private static void moveForward(int[] arr, int start, int end) {
    while (start != end) {
      int temp = arr[start - 1];
      arr[start - 1] = arr[start];
      arr[start] = temp;
      start--;
    }
  }

  private static void shuffle(int[] arr, int p) {
    int shuffleLen;
    
    if (p > arr.length / 2) {
      shuffleLen = arr.length - p;
      for (int i = p; i < arr.length; i++)
        moveForward(arr, i, i + arr.length - 2 * p);
    }
    else
      shuffleLen = p;
    
    for (int i = 0; i < shuffleLen; i++) {
      moveForward(arr, shuffleLen + i, 2 * i + 1);
    }
  }
  
  public static void main(String[] args)
  {
    int[] arr = new int[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    shuffle(arr, 8);
    
    for (int i : arr)
      System.out.print(i + " ");
  }
}
