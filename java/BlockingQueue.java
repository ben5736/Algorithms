import java.util.LinkedList;
import java.util.concurrent.atomic.AtomicInteger;

public class BlockingQueue {

	private LinkedList<Integer> list;

	public BlockingQueue() {
		list = new LinkedList<Integer>();
	}

	public synchronized void add(int value) {
		list.addLast(value);
		if (list.size() == 1) notify();
	}

	public synchronized int remove() throws InterruptedException {
		if (list.isEmpty())
			wait();

		return list.removeFirst();
	}

	static class Producer implements Runnable {
		private static int n = 0;
		private static AtomicInteger atomicInt = new AtomicInteger(0);
		int i;
		BlockingQueue queue;

		Producer(BlockingQueue queue) {
			this.queue = queue;
			i = ++n;
		}

		@Override
		public void run() {
			try {
				while (true) {
					int v = atomicInt.getAndAdd(1);
					System.out.println("Producer " + i + " inserted " + v);
					queue.add(v);
					//Thread.sleep(new Random().nextInt(400) + 700);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

	static class Consumer implements Runnable {
		private static int n = 0;
		int i;
		BlockingQueue queue;

		Consumer(BlockingQueue queue) {
			this.queue = queue;
			i = ++n;
		}

		@Override
		public void run() {
			try {
				while (true) {
					int v = queue.remove();
					System.out.println("Consumer " + i + " inserted " + v);
					//Thread.sleep(new Random().nextInt(400) + 300);
				}
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

	public static void main(String[] args) {
		BlockingQueue queue = new BlockingQueue();
		for (int i = 0; i < 10; i++) {
			new Thread(new Producer(queue)).start();
			new Thread(new Consumer(queue)).start();
		}

		while (true)
			;
	}
}
