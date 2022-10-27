import java.util.Scanner;

class solutions {

    public static  void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Get number of lines from input to check
        int numLines = in.nextInt();
        in.nextLine();

        // Get the search key
        String searchKey = in.nextLine();

        for (int i = 0; i < numLines; i++) {
            String line = in.nextLine();
            int counter = countLine(line, searchKey);
            // Print result
            System.out.println(counter);
        }

        in.close();
    }

    // Count number of times the search key is in the line
    public static int countLine(String line, String searchKey) {
        int counter = 0;
        // Valid places where the search key can start (cannot fit if in the last four characters)
        for (int i = 0; i < line.length(); i++) {
            // Find the first character of the search key
            if (line.charAt(i) == searchKey.charAt(0) && i <= line.length() - searchKey.length()) {
                // Make sure the following characters match the search key
                boolean match = true;
                for (int j = 1; j < searchKey.length(); j++) {
                    if (line.charAt(i + j) != searchKey.charAt(j)) {
                        match = false;
                    }
                }
                if (match) {
                    counter++;
                }
            }
        }
        return counter;
    }
}