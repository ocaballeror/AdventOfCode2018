#include <iostream>

extern long high_score(int, int);
extern void parse_input(int&, int&);

int main(){
    int players, goal;
    parse_input(players, goal);
    goal *= 100;

    std::cout << players << " " << goal << std::endl;

    std::cout << high_score(players, goal) << std::endl;
}
