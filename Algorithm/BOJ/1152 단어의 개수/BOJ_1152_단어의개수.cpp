#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;

int main() {
    string str;
    getline(cin, str,'\n');
    int num = 1;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == ' ')
            ++num;
    }
    if (str[0] == ' ') --num;
    if (str[str.length() - 1] == ' ') --num;

    printf("%d", num);
}

/*
// 오답 모음집

char text[1000001];

int main() {
    cin.getline(text, 1000000, '\n');
    int answer = 1;
    // strlen ... 길이를 제공합니다.
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == ' ') {
            ++answer;
        }
        if (text[0] == ' ')--answer;
        if (text[strlen(text) - 1] == ' ')--answer;
    }
    cout << answer;
    return 0;
}


int main()
{
    // \n 입력 전까지 계속 입력 받습니다. 공백 포함
    cin.getline(text, 1000000,'\n');
    bool isText = false;
    int answer = 1;
    // strlen ... 길이를 제공합니다.
    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == ' ') {
            isText = false;
        }
        else {
            if (!isText) {
                isText = true;
                ++answer;
            }
        }
    }
    cout << answer;
    return 0;
}

*/