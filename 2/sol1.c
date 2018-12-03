#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
	int twos = 0, threes = 0;
	char *word = NULL;
	size_t len, read;
	FILE *file = fopen("input", "r");
	while ((read = getline(&word, &len, file)) != -1) {
		int two = 0;
		int three = 0;
		for (int i=0; i<strlen(word); i++){
			int count = 1;
			for (int j=0; j<strlen(word); j++){
				if (i == j) continue;
				count += (word[i] == word[j]);
			}
			if(count == 2) two = 1;
			if(count == 3) three = 1;
		}
		if(two) twos++;
		if(three) threes++;
	}
	fclose(file);
	if(word) free(word);
	printf("%d * %d = %d\n", twos, threes, twos * threes);
	return 0;
}

