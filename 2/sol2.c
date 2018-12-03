#include <string.h>
#include <stdio.h>
#include <stdlib.h>


int isclose(char *a, char *b, size_t len){
	int diff = 0;
	for(int i=0; i<len; i++){
		if(a[i] != b[i]){
			if(diff){
				return 0;
			}
			diff = 1;
		}
	}

	return diff;
}


char *intersec(char *a, char *b, size_t len){
	char *ret = malloc(sizeof(char) * len);
	for(int i=0; i<len; i++){
		if(a[i] == b[i])
			ret[i] = a[i];
	}
	
	return ret;
}


int main(){
	int twos = 0, threes = 0;
	char *word = NULL;
	size_t len, read;
	FILE *file = fopen("input", "r");

	int linecount = 0;
	int max_len = 0;
	while ((read = getline(&word, &len, file)) != -1){
		linecount ++;
		if(read > max_len)
			max_len = read;
	}	
	fseek(file, 0, SEEK_SET);
	
	char** lines = malloc(sizeof(char*)*linecount);
	for(int i=0; i<linecount; i++){
		read = getline(&word, &len, file);
		if(word[read-1] == '\n'){
			word[read-1] = 0;
		}
		lines[i] = (char*)malloc(sizeof(char*)*read);
		memset(lines[i], 0, read);
		strncpy(lines[i], word, read);
	}

	for(int i=0; i<linecount; i++){
		for(int j=i; j<linecount; j++){
			if(i == j) continue;
			if(isclose(lines[i], lines[j], max_len)){
				char *inter = intersec(lines[i], lines[j], max_len);
				printf("Solution: %s\n", inter);
				free(inter);
			}
		}
		free(lines[i]);
	}

	fclose(file);
	if(word) free(word);
	if(lines) free(lines);
	return 0;
}

