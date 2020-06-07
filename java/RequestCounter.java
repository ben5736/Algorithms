import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class RequestCounter {
  private int[] counters = new int[3600];
  private int minuteCounter = 0;
  private int hourCounter = 0;
  private int curSlot = 0;
  private Timer timer;

  public RequestCounter() {
    timer = new Timer();
    timer.schedule(new TimerTask() {
      @Override
      public void run() {
        advanceSlot();
      }
    }, 1000, 1000);
  }

  synchronized public void increment() {
    counters[curSlot]++;
    minuteCounter++;
    hourCounter++;
  }

  public int getMinuteCount() {
    return minuteCounter;
  }

  public int getSecondCount() {
    return counters[curSlot];
  }

  public int getHourCount() {
    return hourCounter;
  }

  synchronized private void advanceSlot() {
    int nextSlot = curSlot == counters.length - 1 ? 0 : curSlot + 1;

    hourCounter -= counters[nextSlot];
    minuteCounter -= curSlot - 59 >= 0 ? counters[curSlot - 59]
        : counters[curSlot - 59 + counters.length];
    counters[nextSlot] = 0;
    curSlot = nextSlot;
  }

  public static void main(String[] args) throws InterruptedException {
    final RequestCounter c = new RequestCounter();

    new Timer().schedule(new TimerTask() {
      private int i = 0;
      
      @Override
      public void run() {
        System.out.format("%d: %d %d\n", i++, c.getSecondCount(), c.getMinuteCount());
      }
    }, 500, 500);
  
    Random r = new Random();
    while (true) {
      c.increment();
      Thread.sleep(r.nextInt(100));
    }
  }
}
