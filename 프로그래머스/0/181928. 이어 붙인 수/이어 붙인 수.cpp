#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(vector<int> num_list) {
    int e = 0, o = 0, answer = 0;
    
    for (int i = num_list.size() - 1; i >= 0; i--) {
        if (num_list[i] % 2) {
            // 홀수면
            answer += num_list[i] * pow(10, o);
            o++;
        } else {
            answer += num_list[i] * pow(10, e);
            e++;
        }
    }
    return answer;
}