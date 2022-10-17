import java.util.Scanner;

class solutions {

    public static  void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Get number of lines from input to check
        String lengths = in.nextLine();
        String[] lengths_split = lengths.split(" ");
        int numLines = Integer.parseInt(lengths_split[0]);
        int numKeys = Integer.parseInt(lengths_split[1]);

        // Get the search key
        String searchKeyLine = in.nextLine();
        String[] searchKeys;
        if (searchKeyLine.contains(";")) {
            searchKeys = searchKeyLine.split(";");
        } else {
            String[] key = {searchKeyLine};
            searchKeys = key;
        }

        for (int i = 0; i < numLines; i++) {
            int[] counters = new int[numKeys];
            String line = in.nextLine();
            for (int j = 0; j < numKeys; j++) {
                int count = countLine(line, searchKeys[j]);
                counters[j] = count;
            }
            for (int j = 0; j < counters.length - 1; j++) {
                System.out.print(counters[j] + " ");
            }
            System.out.println(counters[counters.length - 1]);
        }

        in.close();
    }

    // Count number of times "Romeo" is in the line
    public static int countLine(String line, String searchKey) {
        int counter = 0;
        // Valid places where "Romeo" can start (cannot fit if in the last four characters)
        for (int i = 0; i < line.length(); i++) {
            // Find "R"
            if (line.charAt(i) == searchKey.charAt(0) && i <= line.length() - searchKey.length()) {
                // Make sure the following characters match "omeo"
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