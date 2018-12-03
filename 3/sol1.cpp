#include <iostream>
#include <fstream>
#include <cstdio>
#include <unordered_map>
#include <unordered_set>


int main() {
	int count = 0;
	std::ifstream in("input");
	std::string line;
	std::unordered_map<int, std::unordered_set<int> > covered;
	while(std::getline(in, line)){
		int left, top, width, height;
		sscanf(line.c_str(), "%*s @ %d,%d: %dx%d", &left, &top, &width, &height);
		for(int i=left; i<left+width; i++){
			for(int j=top; j<top+height; j++){
				if(covered[i].count(j)){
					count++;
				} else {
					covered[i].insert(j);
				}
			}
		}
	}

	std::cout << "count: " << count << std::endl;
	return 0;
}

