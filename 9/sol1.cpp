#include <iostream>

extern unsigned long high_score(int, int);
extern void parse_input(int&, int&);

int main(){
    int players, goal;
    parse_input(players, goal);

    std::cout << high_score(players, goal) << std::endl;
}
