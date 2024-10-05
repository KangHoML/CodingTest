#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

"""
    동영상 재생기
    https://school.programmers.co.kr/learn/courses/30/lessons/340213
"""

int time_to_sec(const char* time) {
    int min, sec;
    sscanf(time, "%d:%d", &min, &sec);
    
    return min * 60 + sec;
}

void sec_to_time(int sec, char* time) {
    int min = sec / 60;
    sec %= 60;

    sprintf(time, "%02d:%02d", min, sec);
}

char* solution(const char* video_len, const char* pos, const char* op_start, const char* op_end, const char** commands, size_t commands_len) {
    int tot_time = time_to_sec(video_len);
    int cur_time = time_to_sec(pos);
    int start_time = time_to_sec(op_start);
    int end_time = time_to_sec(op_end);

    for (size_t i = 0; i < commands_len; i++) {
        // 오프팅 건너뛰기
        if (cur_time >= start_time && cur_time <= end_time)
            cur_time = end_time;
            
        // 명령어 수행
        if (strcmp(commands[i], "prev") == 0)
            cur_time = (cur_time > 10) ? cur_time - 10 : 0;
        else
            cur_time = (cur_time + 10 < tot_time) ? cur_time + 10 : tot_time;
    }
    
    // 오프팅 건너뛰기
    if (cur_time >= start_time && cur_time <= end_time)
        cur_time = end_time;
    
    // 결과 출력
    char* result = (char*)malloc(6 * sizeof(char));
    sec_to_time(cur_time, result);
    
    return result;
}