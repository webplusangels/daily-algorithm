#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int num, int n) {
    if (num % n) {
        return 0;
    }
    else { return 1; }
}