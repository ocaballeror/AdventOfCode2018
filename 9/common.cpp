#include <fstream>
#include <cmath>
#include <list>
#include <exception>

unsigned long max(unsigned long *list, int size){
    unsigned long best = (unsigned long)-INFINITY;
    for (int i=0; i<size; i++){
        if(list[i] > best){
            best = list[i];
        }
    }

    return best;
}

unsigned long high_score(int players, int goal){
    std::list<int> marbles(1, 0);
    auto marbles_it = marbles.begin();
    int current_player = 0;
    unsigned long scores[players] = {0UL};

    for(int i=1; i<=goal; i++){
        if(i % 23 != 0){
            marbles_it ++;
            if(marbles_it == marbles.begin()) marbles_it++;
            marbles.insert(marbles_it, i);
        } else {
            bool lap = false;
            for (int i=0; i<8; i++){
                marbles_it--;
                if(marbles_it == marbles.begin()) lap = true;
            }
            if(lap) marbles_it--;

            int pop = *marbles_it;
            marbles_it = marbles.erase(marbles_it);
            ++marbles_it;
            scores[current_player] += (pop + i);
        }
        current_player = (current_player + 1) % players;
    }
    return max(scores, players);
}

void parse_input(int &players, int &goal){
    std::string dummy;
    std::ifstream in("input");
    in >> players;
    while(true){
        try {
            in >> dummy;
            goal = std::stoi(dummy);
            break;
        } catch (std::exception &e){}
    }
}
