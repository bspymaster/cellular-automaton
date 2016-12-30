# cellular-automaton
A small project using procedural generation to make interesting designs.

This script takes each existing cell in a matrix and sums up all the cells around it, including itself (9 total cells will be summed).
The result of the sum dictates what the value of the cell will be in the next iteration:
 * If the number of cells with a `1` is **even**, the value of the cell will be `1` (represented by a `#`) in the next iteration of the matrix.
 * If the number of cells with a `1` is **odd**, the value of the cell will be `0` (represented by a `#`) in the next iteration of the matrix.

If the adjacent cell to the working cell is nonexistent (outside the matrix), it uses a cell from a predestined "supercell" next to it. modifying these supercell values acts as a "seed" for the patterns that emerge over time. The dimensions of the matrix also changes the pattern and duration of the automaton.

An example sequence of an 8x8 matrix with the seed `000 0 0 000`:

![](https://i.imgur.com/PjwP7I2.gif)
