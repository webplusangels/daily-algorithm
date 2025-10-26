#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int last = num_list.back();
    int second_last = num_list[num_list.size() - 2];
    
    if (last > second_last) {
        num_list.push_back(last - second_last);
    } else {
        num_list.push_back(2*last);
    }
    
    return num_list;
}