import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Graph {
	enum Mark
	{
		//unvisited,
		visiting,
		visited
	}
	
	ArrayList<GraphNode> nodes = new ArrayList<GraphNode>();

	public void dfs(VisitMethod visitMethod) {
		Stack<GraphNode> stack = new Stack<GraphNode>();
		HashSet<GraphNode> visited = new HashSet<GraphNode>();

		for (GraphNode node : nodes) {
			if (!visited.contains(node)) {
				stack.push(node);
				while (!stack.isEmpty()) {
					GraphNode cur = stack.pop();
					visitMethod.visit(cur);
					visited.add(cur);

					for (GraphNode neighbor : cur.neighbors)
						if (!visited.contains(neighbor))
							stack.push(neighbor);
				}
			}
		}
	}
	
	public void topological(VisitMethod visitMethod)
	{
		Stack<GraphNode> stack = new Stack<GraphNode>();
		HashMap<GraphNode, Mark> marks = new HashMap<GraphNode, Mark>();
		ArrayList<GraphNode> sorted = new ArrayList<GraphNode>();
		
		for (GraphNode node : nodes) {
			if (!marks.containsKey(node)) {
				stack.push(node);
				while (!stack.isEmpty()) {
					GraphNode cur = stack.peek();
					if (marks.get(cur) == Mark.visiting)
					{
						stack.pop();
						marks.put(cur, Mark.visited);
						sorted.add(cur);
					}
					else
					{
						marks.put(cur, Mark.visiting);

						for (GraphNode neighbor : cur.neighbors)
							if (!marks.containsKey(neighbor))
								stack.push(neighbor);	
					}
				}
			}
		}
		
		for (int i = sorted.size() - 1; i >= 0; i--)
			visitMethod.visit(sorted.get(i));
	}

	public void bfs(VisitMethod visitMethod) {
		Queue<GraphNode> queue = new LinkedList<GraphNode>();
		HashSet<GraphNode> visited = new HashSet<GraphNode>();

		for (GraphNode node : nodes) {
			if (!visited.contains(node)) {
				queue.add(node);
				while (!queue.isEmpty()) {
					GraphNode cur = queue.remove();
					visitMethod.visit(cur);
					visited.add(cur);

					for (GraphNode neighbor : cur.neighbors)
						if (!visited.contains(neighbor))
							queue.add(neighbor);
				}
			}
		}
	}

	void add(GraphNode... nodes) {
		for (GraphNode node : nodes)
			this.nodes.add(node);
	}

	public static void main(String[] args) {
		GraphNode node7 = new GraphNode(7);
		GraphNode node5 = new GraphNode(5);
		GraphNode node3 = new GraphNode(3);
		GraphNode node11 = new GraphNode(11);
		GraphNode node8 = new GraphNode(8);
		GraphNode node2 = new GraphNode(2);
		GraphNode node9 = new GraphNode(9);
		GraphNode node10 = new GraphNode(10);

		node7.addNeighbors(node11, node8);
		node5.addNeighbors(node11);
		node3.addNeighbors(node8, node10);
		node11.addNeighbors(node2, node9, node10);
		node8.addNeighbors(node9);
		
		Graph g = new Graph();
		g.add(node7, node5, node3, node11, node8, node2, node9, node10);
		g.dfs(new Print());
		System.out.println();
		g.bfs(new Print());
		System.out.println();
		g.topological(new Print());
		System.out.println();
	}
}

class GraphNode {
	int val;
	ArrayList<GraphNode> neighbors = new ArrayList<GraphNode>();

	GraphNode(int val) {
		this.val = val;
	}

	void addNeighbors(GraphNode... neighbors) {
		for (GraphNode neighbor : neighbors)
			this.neighbors.add(neighbor);
	}
}

interface VisitMethod {
	void visit(GraphNode node);
}

class Print implements VisitMethod {

	@Override
	public void visit(GraphNode node) {
		System.out.print(node.val);
		System.out.print(" ");
	}

}