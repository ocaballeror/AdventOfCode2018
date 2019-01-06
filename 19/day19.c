#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
char* operation_names[16] = {
	"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
	"setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"
};

int indexof(int *list, int size, int elem){
	for (int i=0; i<size; i++){
		if(list[i] == elem) return i;
	}
	return -1;
}
int str_indexof(char **list, int size, char *elem){
	for (int i=0; i<size; i++){
		if(!strcmp(list[i], elem)) return i;
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
	*instructions = malloc((sizeof(instruction_t) * (lines - 1)));
	fscanf(input, "#ip %d\n", ip_reg);
	for(int i = 0; i < lines - 1; i++) {
		instruction_t line;
		fscanf(input, "%s %d %d %d\n", line.op_name, &line.a, &line.b, &line.c);
		int index = str_indexof(operation_names, 16, line.op_name);
		line.operation = operations[index];
		(*instructions)[i] = line;
	}
	fclose(input);

	return lines - 1;
}

void run_instructions(instruction_t *instructions, int n_instructions, int ip_reg) {
	int ip = 0;
	int count = 0;
	while(1) {
		ip = registers[ip_reg];
		if(ip >= n_instructions)
			break;
		instruction_t next = instructions[ip];
		next.operation(next.a, next.b, next.c);
		registers[ip_reg]++;
	}
}

void run_part2(instruction_t *instructions, int n_instructions, int ip_reg) {
	int ip = 0;
	int count = 0;
	while(1) {
		ip = registers[ip_reg];
		if(ip >= n_instructions)
			break;
		instruction_t next = instructions[ip];
		next.operation(next.a, next.b, next.c);
		registers[ip_reg]++;

		/*
		 * Ok, so here's the deal. After a few instructions, the registers will stabilize
		 * more or less, increasing r4 every few million operations until it reaches r5, 
		 * which, for my input has a value of 10551417 (had to print this out
		 * to figure it out).
		 *
		 * r0 (our puzzle solution) will only change when r4*r1 == r5, meaning
		 * that we have to wait for r4 to slowly reach the divisors of r5.
		 * Luckily r5 only has 2 divisors: 3 and 3517139, so we do the trick
		 * here. Instead of waiting for r4 to reach those high numbers, we wait
		 * until it reaches 4 (meaning that it's already gone through the first
		 * divisor, which is 3), and manually set it to the next divisor. When
		 * r4 has surpassed that number, there won't be any divisors left, so
		 * we skip to r5 - 1 and watch it reach the actual value of r5 and
		 * finish the program.
		 *
		 * Kind of a hacky solution, mostly because it only works for my input,
		 * but heck, I got the answer right :)
		 * */
		if (count++ % 100000 == 0) { // This is just to avoid printing on every iteration
			/* printf("[%d %d %d %d %d %d]\n", registers[0], registers[1], registers[2], registers[3], registers[4], registers[5]); */
			if(registers[0] == 4 && registers[5] == 10551417)
				registers[4] = 3517138;
			if(registers[4] == 3517140)
				registers[4] = registers[5] - 1;
		}
	}
}

int main() {
	int ip_reg = 0;
	instruction_t *instructions = NULL;
	int n_instructions = read_instructions(&ip_reg, &instructions);
	run_instructions(instructions, n_instructions, ip_reg);
	printf("Part 1: %d\n", registers[0]);

	for (int i=1; i<6; i++){
		registers[i] = 0;
	}
	registers[0] = 1;
	run_part2(instructions, n_instructions, ip_reg);
	printf("Part 2: %d\n", registers[0]);
	free(instructions);
	return 0;
}
