#include <iostream>
#include <fstream>
#include <cstdio>
#include <unordered_map>


template <>
struct std::hash<std::pair<int, int> > {
    public:
        size_t operator()(std::pair<int, int> x) const throw() {
            size_t h = 13 + (x.first*39+x.second*39);//something with x
            return h;
        }
};

int main() {
    std::ifstream in("input");
    std::string line;
    std::unordered_map<std::pair<int, int>, int> covered;
    while(std::getline(in, line)){
        int left, top, width, height;
        sscanf(line.c_str(), "%*s @ %d,%d: %dx%d", &left, &top, &width, &height);
        for(int i=left; i<left+width; i++){
            for(int j=top; j<top+height; j++){
                std::pair<int, int> key = std::make_pair(i, j);
                if(covered.count(key)){
                    covered[key]++;
                } else {
                    covered[key] = 1;
                }
            }
        }
    }

    int count = 0;
    for(auto it=covered.cbegin(); it!=covered.cend(); it++){
        if(it->second > 1) count++;
    }
    std::cout << "count: " << count << std::endl;
    return 0;
}
