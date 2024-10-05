#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

"""
    퍼즐 게임 챌린지
    https://school.programmers.co.kr/learn/courses/30/lessons/340212
"""

bool is_possible(int diffs[], size_t diffs_len, int times[], size_t times_len, long long limit, int level) {
    long long time = times[0];

    for(int i = 1; i < diffs_len; i++) {
        if (diffs[i] <= level)
            time += times[i];
        else
            time += ((diffs[i] - level) * (times[i-1] + times[i]) + times[i]);
        
        if (time > limit) return false;
    }

    return true;
}

int solution(int diffs[], size_t diffs_len, int times[], size_t times_len, long long limit) {
    int min_lev = 1;
    int max_lev = 100000;
    
    // 이진 탐색
    while(min_lev <= max_lev) {
        int mid_lev = min_lev + (max_lev - min_lev) / 2;

        if (is_possible(diffs, diffs_len, times, times_len, limit, mid_lev))
            max_lev = mid_lev - 1;
        else
            min_lev = mid_lev + 1;
    }

    return min_lev;
}
