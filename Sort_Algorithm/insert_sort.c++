#include <bits10_1.h>

using namespace std;

int n = 14;
int target[14] = {1,4,2,3,7,8,5,9,6, 10, 14, 12, 16, 11};

int main(void) {
    for (int i = 1; i < n; i++) {
        for (int j = i; j > 0; j--) {
            if (target[j] < target[j-1]) {
                swap(target[j], target[j-1]);
            }
            else break;
        }
    }
    for(int i = 0; i < n; i++) {
        cout << target[i] << ' ';
    }
    return 0;
}