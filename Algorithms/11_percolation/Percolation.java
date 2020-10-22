import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private boolean[][] grid;
    private WeightedQuickUnionUF wqfGrid;
    private WeightedQuickUnionUF wqfFull;
    private int gridSize;
    private int gridSquared;
    private int virtualTop;
    private int virtualBottom;
    private int openSites;

    public Percolation(int n) {
        if (n <= 0) throw new IllegalArgumentException("N must be > 0");
        gridSize = n;
        gridSquared = n * n;
        grid = new boolean[gridSize][gridSize];
        wqfGrid = new WeightedQuickUnionUF(gridSquared + 2); // includes virtual top bottom
        wqfFull = new WeightedQuickUnionUF(gridSquared + 1); // includes virtual top
        virtualBottom = gridSquared + 1;
        virtualTop = gridSquared;
        openSites = 0;

    }

    public void open(int row, int col) {
        validateSite(row, col);

        int shiftRow = row - 1;
        int shiftCol = col - 1;
        int flatIndex = flattenGrid(row, col) - 1;

        if (isOpen(row, col)) {
            return;
        }


        grid[shiftRow][shiftCol] = true;
        openSites++;

        if (row == 1) {  // Top Row
            wqfGrid.union(virtualTop, flatIndex);
            wqfFull.union(virtualTop, flatIndex);
        }

        if (row == gridSize) {  // Bottom Row
            wqfGrid.union(virtualBottom, flatIndex);
        }

        if (isOnGrid(row, col - 1) && isOpen(row, col - 1)) {
            wqfGrid.union(flatIndex, flattenGrid(row, col - 1) - 1);
            wqfFull.union(flatIndex, flattenGrid(row, col - 1) - 1);
        }

        if (isOnGrid(row, col + 1) && isOpen(row, col + 1)) {
            wqfGrid.union(flatIndex, flattenGrid(row, col + 1) - 1);
            wqfFull.union(flatIndex, flattenGrid(row, col + 1) - 1);
        }

        if (isOnGrid(row - 1, col) && isOpen(row - 1, col)) {
            wqfGrid.union(flatIndex, flattenGrid(row - 1, col) - 1);
            wqfFull.union(flatIndex, flattenGrid(row - 1, col) - 1);
        }

        if (isOnGrid(row + 1, col) && isOpen(row + 1, col)) {
            wqfGrid.union(flatIndex, flattenGrid(row + 1, col) - 1);
            wqfFull.union(flatIndex, flattenGrid(row + 1, col) - 1);
        }

        // runTests();
    }

    public boolean isOpen(int row, int col) {
        validateSite(row, col);
        return grid[row - 1][col - 1];

    }

    public boolean isFull(int row, int col) {
        validateSite(row, col);
        return wqfFull.connected(virtualTop, flattenGrid(row, col) - 1);
    }

    public int numberOfOpenSites() {
        return openSites;
    }

    public boolean percolates() {
        return wqfGrid.connected(virtualTop, virtualBottom);
    }

    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);

        Percolation percolation = new Percolation(size);
        int argCount = args.length;
        for (int i = 1; argCount >= 2; i += 2) {
            int row = Integer.parseInt(args[i]);
            int col = Integer.parseInt(args[i + 1]);
            StdOut.printf("Adding row: %d  col: %d %n", row, col);
            percolation.open(row, col);
            if (percolation.percolates()) {
                StdOut.printf("%nThe System percolates %n");
            }
            argCount -= 2;
        }
        if (!percolation.percolates()) {
            StdOut.print("Does not percolate %n");
        }

    }

    private int flattenGrid(int row, int col) {
        return gridSize * (row - 1) + col;
    }

    private void validateSite(int row, int col) {
        if (!isOnGrid(row, col)) {
            throw new IndexOutOfBoundsException("Index is out of bounds");
        }
    }

    private boolean isOnGrid(int row, int col) {
        int shiftRow = row - 1;
        int shiftCol = col - 1;
        return (shiftRow >= 0 && shiftCol >= 0 && shiftRow < gridSize && shiftCol < gridSize);
    }

    /* private void runTests() {
        for (int row = 1; row <= gridSize; row++) {
            for (int col = 1; col <= gridSize; col++) {
                if (isOpen(row, col)) {
                    StdOut.printf("Row: %d Col: %d is Open %n", row, col);
                } else {
                    StdOut.printf("Row: %d Col: %d is not Open %n", row, col);
                }
                if (isFull(row, col)) {
                    StdOut.printf("Row: %d Col: %d is Full %n", row, col);
                } else {
                    StdOut.printf("Row: %d Col: %d is not Full %n", row, col);
                }
            }
        }
        StdOut.printf("Sites Open: %d %n", numberOfOpenSites());
        if (percolates()) {
            StdOut.printf("Percolates %n");
        } else {
            StdOut.printf("Does not Percolate %n");
        }
    }
*/
}
