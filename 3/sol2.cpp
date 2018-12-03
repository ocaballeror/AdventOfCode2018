#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <unordered_set>


int main() {
	std::ifstream in("input");
	std::string line;
	// maps coordinates to claim ids.
	// uses a bidimensional map as a workaround to using pairs as keys
	std::unordered_map<int, std::unordered_map<int, int> > covered;
	// good guys are those ids that don't overlap with anyone
	std::unordered_set<int> good_guys;

	while(std::getline(in, line)){
		int id, left, top, width, height;
		sscanf(line.c_str(), "#%d @ %d,%d: %dx%d", &id, &left, &top, &width, &height);
		bool is_good_guy = true;
		for(int i=left; i<left+width; i++){
			for(int j=top; j<top+height; j++){
				if(covered[i].count(j)){
					// if it's already covered, remove the author from the good guys list
					// and mark ourselves as "not a good guy"
					int author = covered[i][j];
					if(good_guys.count(author)){
						good_guys.erase(author);
					}
					is_good_guy = false;
				} else {
					// if nobody else has claimed this sq inch, mark it as our own.
					covered[i][j] = id;
				}
			}
		}
		if(is_good_guy) good_guys.insert(id);
	}

	std::cout << "good guys: ";
	for(auto &x : good_guys){
		std::cout << x <<", ";
	}
	std::cout << std::endl;
	return 0;
}

