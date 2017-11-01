import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;


public class MinHeap {
	public static void main(String[] args)
	{
		MinHeap heap = new MinHeap();
		
		Random r = new Random();
		for (int i = 0; i < 10000; i++)
		{
			heap.add(r.nextInt(25));
			if (!heap.isValid())
				System.out.println(i + " Invalid!");
			heap.add(r.nextInt(25));
			if (!heap.isValid())
				System.out.println(i + " Invalid!");
			heap.remove(r.nextInt(25));
			if (!heap.isValid())
				System.out.println(i + " Invalid!");
		}
	}
	
	private ArrayList<Integer> heap = new ArrayList<Integer>();
	private HashMap<Integer, HashSet<Integer>> indexMap = new HashMap<Integer, HashSet<Integer>>();
	
	private int getParent(int i)
	{
		return (i - 1) / 2;
	}
	
	private int getLeftChild(int i)
	{
		return 2 * i + 1;
	}
	
	private int getRightChild(int i)
	{
		return 2 * i + 2;
	}
	
	public void add(int e)
	{
		heap.add(e);
		int cur = heap.size() - 1;
		insertIndexMap(e, cur);
		int parent = getParent(cur);
		
		while (heap.get(parent) > heap.get(cur))
		{
			int temp = heap.get(parent);
			
			heap.set(parent, heap.get(cur));
			updateIndexMap(heap.get(parent), cur, parent);
			
			heap.set(cur, temp);
			updateIndexMap(heap.get(cur), parent, cur);
			
			cur = parent;
			parent = getParent(cur);
		}
	}
	
	public Integer peek()
	{
		if (heap.isEmpty())
			return null;
		else
			return heap.get(0);
	}
	
	public void remove(int e)
	{
		HashSet<Integer> indexes = indexMap.get(e);
		
		if (indexes == null)
			return;
		
		int cur = indexes.iterator().next();
		if (cur == heap.size() - 1)
		{
			removeIndexMap(e, cur);
			heap.remove(heap.size() - 1);
			return;
		}
		
		heap.set(cur, heap.get(heap.size() - 1));
		removeIndexMap(e, cur);
		updateIndexMap(heap.get(cur), heap.size() - 1, cur);
		heap.remove(heap.size() - 1);
		
		
		int parent = getParent(cur);
		
		while (heap.get(parent) > heap.get(cur))
		{
			int temp = heap.get(parent);
			
			heap.set(parent, heap.get(cur));
			updateIndexMap(heap.get(parent), cur, parent);
			
			heap.set(cur, temp);
			updateIndexMap(heap.get(cur), parent, cur);
			
			cur = parent;
			parent = getParent(cur);
		}
		
		int left = getLeftChild(cur);
		int right = getRightChild(cur);
		
		while ((left < heap.size() && heap.get(cur) > heap.get(left)) 
				|| (right < heap.size() && heap.get(cur) > heap.get(right)))
		{
			int tar = (right < heap.size() && heap.get(right) < heap.get(left)) ? right : left;
			int temp = heap.get(tar);
			
			heap.set(tar, heap.get(cur));
			updateIndexMap(heap.get(tar), cur, tar);
			
			heap.set(cur, temp);
			updateIndexMap(heap.get(cur), tar, cur);
			
			cur = tar;
			left = getLeftChild(cur);
			right = getRightChild(cur);
		}
	}
	
	public boolean isValid()
	{
		for (int i = heap.size() - 1; i >= 0; i--)
		{
			if (heap.get(i) < heap.get(getParent(i)))
				return false;
			
			if (!indexMap.get(heap.get(i)).contains(i))
				return false;
		}
		
		return true;
	}

	private void removeIndexMap(int e, int cur) {
		HashSet<Integer> indexes = indexMap.get(e);
		indexes.remove(cur);
		if (indexes.isEmpty())
			indexMap.remove(e);
	}

	private void updateIndexMap(int e, int from, int to) {
		HashSet<Integer> indexes = indexMap.get(e);
		indexes.remove(from);
		indexes.add(to);
	}

	private void insertIndexMap(int e, int cur) {
		HashSet<Integer> indexes = indexMap.get(e);
		
		if (indexes == null)
		{
			indexes = new HashSet<Integer>();
			indexMap.put(e, indexes);
		}
		
		indexes.add(cur);
	}
}
