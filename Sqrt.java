
public class Sqrt {

	private static double sqrt(double x) {
		final double e = 0.00001;
		
		if (x < 0)
			throw new RuntimeException();
		
		double start, end;
		if (x > 1)
		{
			start = 1;
			end = x;
		}
		else
		{
			start = x;
			end = 1;
		}
		
		double mid = (start + end) / 2.0;
		while (Math.abs(x - mid * mid) > e)
		{
			System.out.println(mid);
			if (mid * mid > x)
				end = mid;
			else
				start = mid;
			mid = (start + end) / 2.0;
		}
		return mid;
	}
	
	public static void main(String[] args) {
		System.out.println(sqrt(0.0001));
	}

}
