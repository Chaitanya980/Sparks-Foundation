#include <iostream>// branch and bound vala
#include <vector>
int N;
using namespace std;
void printSol(vector<vector<int> > board)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)

        {
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
}
bool isSafe(int row, int col, vector<bool> rows, vector<bool> left_diagonals, vector<bool> right_diagonals)
{
    if (rows[row] == true || left_diagonals[row + col] == true || right_diagonals[col - row + N - 1] == true)
    {
        return false;
    }
    return true;
}
bool solve(vector<vector<int> > &board, int col, vector<bool> rows, vector<bool> left_diagonals, vector<bool> right_diagonals)
{
    if (col >= N)
    {
        return true;
    }
    for (int i = 0; i < N; i++)
    {
        if (isSafe(i, col, rows, left_diagonals, right_diagonals) == true)
        {
            rows[i] = true;
            left_diagonals[i + col] = true;
            right_diagonals[col - i + N - 1] = true;
            board[i][col] = 1;
            if (solve(board, col + 1, rows, left_diagonals, right_diagonals) == true)
            {
                return true;
            }
            rows[i] = false;
            left_diagonals[i + col] = false;
            right_diagonals[col - i + N - 1] = false;
            board[i][col] = 0;
        }
    }
    return false;
}
int main()
{
    cout << "Enter the no of rows for the square board:";
    cin >> N;
    vector<vector<int> > board(N, vector<int>(N, 0));
    vector<bool> rows(N, false);
    vector<bool> left_diagonals(2 * N - 1, false);
    vector<bool> right_diagonals(2 * N - 1, false);
    bool ans = solve(board, 0, rows, left_diagonals, right_diagonals);
    if (ans == true)
    {
        printSol(board);
    }
    else
    {
        cout << "Solution Does not Exist" << endl;
    }
    return 0;
}