#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unordered_set>

typedef struct {
	void (*operation)(int, int, int);
	char op_name[5];
	int a;
	int b;
	int c;
} instruction_t;

int registers[6];


void addr(int a, int b, int c){
	registers[c] = registers[a] + registers[b];
}
void addi(int a, int b, int c){
	registers[c] = registers[a] + b;
}

void mulr(int a, int b, int c){
	registers[c] = registers[a] * registers[b];
}
void muli(int a, int b, int c){
	registers[c] = registers[a] * b;
}

void banr(int a, int b, int c){
	registers[c] = registers[a] & registers[b];
}
void bani(int a, int b, int c){
	registers[c] = registers[a] & b;
}

void borr(int a, int b, int c){
	registers[c] = registers[a] | registers[b];
}
void bori(int a, int b, int c){
	registers[c] = registers[a] | b;
}

void setr(int a, int _, int c){
	registers[c] = registers[a];
}
void seti(int a, int _, int c){
	registers[c] = a;
}

void gtir(int a, int b, int c){
	registers[c] = a > registers[b];
}
void gtri(int a, int b, int c){
	registers[c] = registers[a] > b;
}
void gtrr(int a, int b, int c){
	registers[c] = registers[a] > registers[b];
}

void eqir(int a, int b, int c){
	registers[c] = a == registers[b];
}
void eqri(int a, int b, int c){
	registers[c] = registers[a] == b;
}
void eqrr(int a, int b, int c){
	registers[c] = registers[a] == registers[b];
}

void (*operations[16])(int, int, int) = {
	addr, addi, mulr, muli, banr, bani, borr, bori,
	setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
};
std::string operation_names[16] = {
	"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
	"setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"
};

int indexof(int *list, int size, int elem){
	for (int i=0; i<size; i++){
		if(list[i] == elem) return i;
	}
	return -1;
}
int str_indexof(std::string *list, int size, std::string elem){
	for (int i=0; i<size; i++){
		if(list[i] == elem) return i;
	}
	return -1;
}


int read_instructions(int *ip_reg, instruction_t **instructions) {
	FILE* input = fopen("input", "r");

	int lines = 0;
	while(!feof(input)) {
		char ch = fgetc(input);
		if(ch == '\n') {
			lines++;
		}
	}
	fseek(input, 0, SEEK_SET);
	*instructions = (instruction_t *)malloc((sizeof(instruction_t) * (lines - 1)));
	fscanf(input, "#ip %d\n", ip_reg);
	for(int i = 0; i < lines - 1; i++) {
		instruction_t line;
		fscanf(input, "%s %d %d %d\n", line.op_name, &line.a, &line.b, &line.c);
		int index = str_indexof(operation_names, 16, std::string(line.op_name));
		line.operation = operations[index];
		(*instructions)[i] = line;
	}
	fclose(input);

	return lines - 1;
}

void run(instruction_t *instructions, int n_instructions, int ip_reg) {
	int ip = 0;
	int last_value = -1;
	std::unordered_set<int> seen;
	while(1) {
		ip = registers[ip_reg];
		if(ip >= n_instructions)
			break;
		/*
		 * This probably won't work for every input.
		 *
		 * Looking at my input code, I realized the program would halt if r3 ==
		 * r0 at instruction 28, so we print the value of r3 the first time we
		 * get there, and we have a solution for part 1.
		 *
		 * Part 2 is more or less the same, instead this time we use a set to
		 * track the values of r3 that we've seen so far. Whenever we see a
		 * repeated value, we are probably going into a loop, so we print the
		 * last "original" one we've seen and exit.
		 * */
		if(ip == 28){
			int value = registers[3];
			if(seen.empty()){
				printf("Part 1: %d\n", value);
			}
			if(!seen.count(value)){
				seen.insert(value);
				last_value = value;
			} else {
				printf("Part 2: %d\n", last_value);
				return;
			}
		}
		instruction_t next = instructions[ip];
		next.operation(next.a, next.b, next.c);
		registers[ip_reg]++;
	}
}

int main() {
	int ip_reg = 0;
	instruction_t *instructions = NULL;
	int n_instructions = read_instructions(&ip_reg, &instructions);
	for (int i=1; i<6; i++){
		registers[i] = 0;
	}
	run(instructions, n_instructions, ip_reg);
	free(instructions);
	return 0;
}
