#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

"""
    충돌위험 찾기
    https://school.programmers.co.kr/learn/courses/30/lessons/340211
"""

// 각 로봇의 상태를 저장
typedef struct {
    int x, y;
    int cur_route;
} Robot;

int solution(int** points, size_t points_rows, size_t points_cols, int** routes, size_t routes_rows, size_t routes_cols) {
    // 충돌 횟수
    int cnt = 0;
    int board[100][100] = {0};
    
    // 각 로봇의 상태 초기화
    Robot* robot = malloc(routes_rows * sizeof(Robot));    
    for (int i = 0; i < routes_rows; i++) {
        robot[i].x = points[routes[i][0]-1][0] - 1;
        robot[i].y = points[routes[i][0]-1][1] - 1;
        robot[i].cur_route = 0;
        board[robot[i].x][robot[i].y]++; 
    }
    
    // 0초일 때 겹치는 상황 고려
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (board[i][j] > 1) cnt++;
            board[i][j] = 0;
        }
    }
    
    bool flag = true;
    while (flag) {
        flag = false;
        
        // 모든 로봇 이동
        for (int i = 0; i < routes_rows; i++) {
            // 이미 루트 종료한 경우 탐색 X
            if (robot[i].cur_route == routes_cols - 1) continue;
            flag = true;
            
            // 다음 목적지
            int np = routes[i][robot[i].cur_route + 1]; // 다음 포인트
            int nx = points[np-1][0] - 1; // 해당 포인트의 행 좌표
            int ny = points[np-1][1] - 1; // 해당 포인트의 열 좌표
            
            
            // x 좌표 이동 -> y 좌표 이동
            if (robot[i].x < nx) robot[i].x++;
            else if (robot[i].x > nx) robot[i].x--;
            else if (robot[i].y < ny) robot[i].y++;
            else if (robot[i].y > ny) robot[i].y--;
            
            // 목적지 도달 시 다음 루트
            if (robot[i].x == nx && robot[i].y == ny) robot[i].cur_route++;
            
            // 로봇 개수 추가
            board[robot[i].x][robot[i].y]++;
        }
        
        // 충돌 횟수 추가
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (board[i][j] > 1) cnt++;
                board[i][j] = 0;
            }
        }
    }
    
    // 메모리 해제
    free(robot);
    
    return cnt;
}