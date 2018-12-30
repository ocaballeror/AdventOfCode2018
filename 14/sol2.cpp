#include <vector>
#include <iostream>
#include <fstream>


bool add_recipes(std::vector<int> &recipes, int first, int second){
    int total = recipes[first] + recipes[second];
    if(total < 10){
        recipes.push_back(total);
        return false;
    }
    recipes.push_back((int) total / 10);
    recipes.push_back(total % 10);
    return true;
}

bool endswith(std::vector<int> &recipes, std::string pattern, bool is_double){
    if(recipes.size() < pattern.size()){
        return false;
    }

    bool equal = true;
    auto it = recipes.rbegin();
    for(auto it2 = pattern.rbegin(); it2 != pattern.rend(); it2++){
        char compare = *it + 48;
        if(compare != *it2){
            equal = false;
            break;
        }
        it++;
    }
    if(equal)
        return true;
    if(!is_double)
        return false;

    equal = true;
    it = recipes.rbegin();
    it++;
    for(auto it2 = pattern.rbegin(); it2 != pattern.rend(); it2++){
        char compare = *it + 48;
        if(compare != *it2){
            equal = false;
            break;
        }
        it++;
    }
    return equal;
}

int sol2(std::string target){
    std::vector<int> recipes({3, 7});
    int first = 0, second = 1;
    bool is_double = add_recipes(recipes, first, second);
    while(!endswith(recipes, target, is_double)){
        is_double = add_recipes(recipes, first, second);
        first = (first + recipes[first] + 1) % recipes.size();
        second = (second + recipes[second] + 1) % recipes.size();
    }

    return recipes.size() - target.size();
}

int main(int argc, char **argv) {
    std::string target;
    std::ifstream input("input");
    if(argc >= 2){
        target = std::string(argv[1]);
    } else {
        input >> target;
    }

    int sol = sol2(target);
    std::cout << sol << std::endl;

	return 0;
}

