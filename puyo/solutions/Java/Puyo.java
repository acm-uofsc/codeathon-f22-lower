import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Puyo {
    static int M;
    static int N;
    static Boolean popFlag;
    static Boolean[][] visits;
    static ArrayList<Coord> popped;
    static ArrayList<Coord> currentChain;
    static int total;

    public class Coord {
        public final Integer m;
        public final Integer n;

        public Coord (Integer m, Integer n) {
            this.m = m;
            this.n = n;
     }
    }

    ArrayList<Coord> popPuyos(int[][] puyoMat) {
        popped = new ArrayList<Coord>();
        popFlag = false;
        total = 0;
        for (int i=0; i < puyoMat.length; i++) {
            for (int j = 0; j < puyoMat[0].length; j++) {
                if (!visits[i][j] && puyoMat[i][j] != 0) {
                    popFlag = false;
                    total = 0;
                    currentChain = new ArrayList<Coord>();
                    this.dfs(i, j, puyoMat);
                    if (popFlag) {
                        popped.addAll(currentChain);
                    }
                }   
            }
        }
        return popped;
    }

    void dfs(int m, int n,
        int[][] puyoMat) {
        visits[m][n] = true;
        currentChain.add(new Coord(m,n));
        total++; // keep count of how many puyos are in this chain
        if (total >= 4) { // 4 is the magic number of puyos that pops the chain
            popFlag = true;
        }

        // we flood fill orthogonal cells where the cells are in bounds,
        // haven't been visted, aren't empty (not 0), and are the same puyo type.
        for (int i=-1; i <= 1; i++) {
            for (int j=-1; j <= 1; j++) {
                if(inBounds(i + m, j + n) && isOrthognol(i, j)
                    && !visits[i + m][j + n] 
                    && puyoMat[m][n] == puyoMat[m + i][n + j]) {
                    dfs(i + m, j + n, puyoMat);
                }
            }
        }
    }

    static Boolean inBounds(int i, int j) {
        if (i >= M || i < 0 || j >= N || j < 0 ) {
            return false;
        }
        return true;    
    }

    static Boolean isOrthognol(int i, int j) {
        if (i == 0 || j == 0) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Puyo puyo = new Puyo();
        Scanner in = new Scanner(System.in);
        M = in.nextInt();
        N = in.nextInt();

        int[][] mat = new int[M][N];
        visits = new Boolean[M][N];

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                mat[i][j] = in.nextInt();
                visits[i][j] = false;
            }
        }

        ArrayList<Coord> popped = puyo.popPuyos(mat);

        popped.sort(
                    (e1, e2) -> {
                        if (e1.m != e2.m)
                            return e1.m.compareTo(e2.m);
                        else
                            return e1.n.compareTo(e2.n);
                    }
        );

        for (Coord e : popped) {
            System.out.println(String.format("%d %d", e.m, e.n));
        }

    }    
}
