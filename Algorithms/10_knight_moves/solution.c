#include <stdio.h>

int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1}, dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int qx[70], qy[70];
int map[9][9];

int main() {
    int sx, sy, ex, ey;
    scanf("%d%d%d%d", &sx, &sy, &ex, &ey);

    int head = 0, tail = 0;
    qx[tail] = sx;
    qy[tail] = sy;
    map[sx][sy] = 1;
    tail++;

    while (head < tail) {
        int x = qx[head];
        int y = qy[head];
        head++;

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 1 || nx > 8 || ny < 1 || ny > 8) continue;

            if (map[nx][ny] == 0) {
                map[nx][ny] = map[x][y] + 1;
                qx[tail] = nx;
                qy[tail] = ny;
                tail++;
            }
        }
    }

    printf("%d", map[ex][ey] - 1);
}