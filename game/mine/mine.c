#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

/** @def MAX_COLS 10 
 * Description
 */
#ifndef MAX_COLS
#define MAX_COLS 10
#endif /* END OF MAX_COLS */ 

/** @def MAX_ROWS 10 
 * Description
 */
#ifndef MAX_ROWS
#define MAX_ROWS 10
#endif /* END OF MAX_ROWS */

/** @var int mine_map[MAX_ROWS][MAX_COLS]
 * Description
 */
int mine_map[MAX_ROWS][MAX_COLS];

/** @var int cover_map[MAX_ROWS][MAX_COLS]
 * Description
 */
int cover_map[MAX_ROWS][MAX_COLS];

/** @var int detectived_mines
 * Description
 */
int detectived_mines = 0;

/** @var int total_mines
 * Description
 */
int total_mines = 20;

int mine_display_ui();
int mine_display_map();
int mine_display_score();

int mine_init();

int main (int argc, char const* argv[])
{
    int dead, x, y, op, i, j;

    mine_init();

    dead = 0;
    do {
        mine_display_ui();
        
        printf("\n");
        printf("op row-position column-position\n");
        printf("op list\n");
        printf("0 - open block\n");
        printf("1 - mark block as mine\n");
        printf("2 - quit game\n");
        printf(" >> ");
        scanf("%d", &op);
        if (op > 2 || op < 0) {
            printf("Not valid op!!\n");
            continue;
        }

        if (op == 2) {
            printf("bye!\n");
            break;
        } else if (op == 1) {
            scanf("%d %d", &x, &y);
            if (x < 0 || x >= MAX_COLS ||
                y < 0 || y >= MAX_ROWS) {
                printf("Not valid x & y!!\n");
            }
            cover_map[x][y] = -1;
            detectived_mines++;
        } else if (op == 0) {
            scanf("%d %d", &x, &y);
            if (x < 0 || x >= MAX_COLS ||
                y < 0 || y >= MAX_ROWS) {
                printf("Not valid x & y!!\n");
            }
            if (cover_map[x][y] == -1) detectived_mines--;
            cover_map[x][y] = 1;
            if (mine_map[x][y] == -1) {
                dead = 1;
                printf("You're dead!!\n");
                for (i = 0; i < MAX_ROWS; i++) {
                    for (j = 0; j < MAX_COLS; j++) {
                        cover_map[i][j] = 1;
                    }
                }
                mine_display_map();
            }
        }
        
    } while (detectived_mines < total_mines && dead == 0);

    return 0;
}

/** init var
 * Description
 * @param 
 * @see 
 * @return 
 */

int mine_init (void)
{
    int i, j, x, y, val;

    memset(mine_map, 0, sizeof(int) * MAX_ROWS * MAX_COLS);
    memset(cover_map, 0, sizeof(int) * MAX_ROWS * MAX_COLS);

    srand((unsigned)time(0));
    for (i = 0; i < total_mines; i++) {
        x = rand() % 10; y = rand() % 10;
        if (mine_map[x][y] == -1) {
            i--;
        } else {
            mine_map[x][y] = -1;
        }
    }

    for (i = 0; i < MAX_ROWS; i++) {
        for (j = 0; j < MAX_COLS; j++) {
            if (mine_map[i][j] == -1) continue;

            if (i-1 < 0 && j-1 < 0) {
                val = (mine_map[i+1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i][j+1] < 0 ? 1 : 0);
            } else if (i-1 < 0 && j+1 >= MAX_COLS) {
                val = (mine_map[i+1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i][j-1] < 0 ? 1 : 0);
            } else if (j-1 < 0 && i+1 >= MAX_ROWS) {
                val = (mine_map[i][j+1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j] < 0 ? 1 : 0);
            } else if (j+1 >= MAX_COLS && i+1 >= MAX_ROWS) {
                val = (mine_map[i][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j] < 0 ? 1 : 0);
            } else if (i-1 < 0) {
                val = (mine_map[i+1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i+1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i][j-1] < 0 ? 1 : 0)
                    + (mine_map[i][j+1] < 0 ? 1 : 0);
            } else if (i+1 >= MAX_ROWS) {
                val = (mine_map[i-1][j] < 0 ? 1 : 0)
                    + (mine_map[i-1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i][j-1] < 0 ? 1 : 0)
                    + (mine_map[i][j+1] < 0 ? 1 : 0);
            } else if (j-1 < 0) {
                val = (mine_map[i][j+1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i+1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j] < 0 ? 1 : 0);
            } else if (j+1 >= MAX_COLS) {
                val = (mine_map[i][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i+1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j] < 0 ? 1 : 0);
            } else {
                val = (mine_map[i][j-1] < 0 ? 1 : 0)
                    + (mine_map[i][j+1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i-1][j] < 0 ? 1 : 0)
                    + (mine_map[i-1][j+1] < 0 ? 1 : 0)
                    + (mine_map[i+1][j] < 0 ? 1 : 0)
                    + (mine_map[i+1][j-1] < 0 ? 1 : 0)
                    + (mine_map[i+1][j+1] < 0 ? 1 : 0);
            }
            mine_map[i][j] = val;
        }
    }

    return 0;
}

/** Display UI
 * Display whole UI
 * @param
 * @see 
 * @return 
 */

int mine_display_ui (void)
{
    mine_display_score();
    mine_display_map();

    return 0;
}

/** Display score
 * display user's score
 * @param 
 * @see 
 * @return 
 */

int mine_display_score (void)
{

    printf("mine: %d/%d\n", detectived_mines, total_mines);

    return 0;
}

/** Display map
 * dispaly map.
 * @param 
 * @see 
 * @return 
 */

int mine_display_map (void)
{
    int i, j;
    char cell_char;

    printf("    ");
    for (i = 0; i < MAX_COLS; i++) {
        printf("%1d ", i);
    }
    printf("\n");
    printf("    ");
    for (i = 0; i < MAX_COLS; i++) {
        printf("- ");
    }
    printf("\n");
    for (i = 0; i < MAX_ROWS; i++) {
        printf("%1d | ", i);
        for (j = 0; j < MAX_COLS; j++) {
            if (cover_map[i][j] == 1 && mine_map[i][j] >= 0 && mine_map[i][j] <= 8) {
                cell_char = mine_map[i][j] + '0';
            } else if (cover_map[i][j] == 1 && mine_map[i][j] == -1) {
                cell_char = '*';
            } else if (cover_map[i][j] == -1) {
                cell_char = '^';
            } else {
                cell_char = '#';
            }
            printf("%1c ", cell_char);
        }
        printf("\n");
    }

    return 0;
}
