#include <unistd.h>
#include <stdio.h>

int registers[4];
int opcodes[16][16];
int misbehavers = 0;


void addr(int a, int b, int c){
	registers[c] = registers[a] +  registers[b];
}
void addi(int a, int b, int c){
	registers[c] = registers[a] + b;
}

void mulr(int a, int b, int c){
	registers[c] = registers[a] *  registers[b];
}
void muli(int a, int b, int c){
	registers[c] = registers[a] * b;
}

void banr(int a, int b, int c){
	registers[c] = registers[a] &  registers[b];
}
void bani(int a, int b, int c){
	registers[c] = registers[a] & b;
}

void borr(int a, int b, int c){
	registers[c] = registers[a] |  registers[b];
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

int read_example(FILE *f, int params[3][4]){
	int* before = params[0];
	int* operation = params[1];
	int* after = params[2];
	int result;
	result = fscanf(f, "Before: [%d, %d, %d, %d]\n", &before[0], &before[1], &before[2], &before[3]);
	if(result == EOF || result < 4)
		return 0;
	fscanf(f, "%d %d %d %d\n", &operation[0], &operation[1], &operation[2], &operation[3]);
	fscanf(f, "After: [%d, %d, %d, %d]\n\n", &after[0], &after[1], &after[2], &after[3]);
	return 1;
}

int equals(int *first, int *second, int size){
	for (int i=0; i<size; i++){
		if(first[i] != second[i])
			return 0;
	}

	return 1;
}

void simulate_ops(int before[4], int operation[4], int after[4]){
	int count = 0;
	int input_op = operation[0];
	for (int i=0; i<16; i++){
		for (int i=0; i<4; i++){
			registers[i] = before[i];
		}
		operations[i](operation[1], operation[2], operation[3]);
		if (equals(registers, after, 4)){
			count++;
			if(opcodes[input_op][i] == -1){
				opcodes[input_op][i] = 1;
			}
		} else {
				opcodes[input_op][i] = 0;
		}
	}
	if(count >= 3)
		misbehavers++;
}

int run_examples(){
	FILE* f = fopen("input", "r");
	int params[3][4];
	while(read_example(f, params)){
		int *before = params[0];
		int *operation = params[1];
		int *after = params[2];
		simulate_ops(before, operation, after);
	}
	int ret = ftell(f);
	fclose(f);
	return ret;
}

int ones(int *list, int size){
	int acc = 0;
	for (int i=0; i<size; i++){
		if(list[i] == 1)
			acc++;
	}
	return acc;
}

int indexof(int *list, int size, int elem){
	for (int i=0; i<size; i++){
		if(list[i] == elem) return i;
	}
	return -1;
}

void guess_opcodes(int real_codes[16]){
	int gotten = 0;
	int old_gotten = -1;
	while(gotten > old_gotten){
		old_gotten = gotten;
		for(int i=0; i<16; i++){
			// If there is only one possible opcode mark it as found and remove it from
			// all the other numbers
			if(ones(opcodes[i], 16) == 1){
				int idx = indexof(opcodes[i], 16, 1);
				/* printf("%d is operation #%d\n", i, idx); */
				real_codes[i] = idx;
				gotten++;
				for (int j=0; j<16; j++){
					opcodes[j][idx] = 0;
				}
			}
		}
	}
}

void sol2(int offset){
	int real_codes[16] = {0};
	void (*real_ops[16])(int, int, int);
	guess_opcodes(real_codes);
	for (int i=0; i<16; i++){
		real_ops[i] = operations[real_codes[i]];
	}
	for (int i=0; i<4; i++){
		registers[i] = 0;
	}

	FILE* f = fopen("input", "r");
	fseek(f, offset, SEEK_SET);
	fscanf(f, "\n\n");
	int op, a, b, c;
	while(fscanf(f, "%d %d %d %d\n", &op, &a, &b, &c) != EOF){
		real_ops[op](a, b, c);
	}
	fclose(f);
	printf("Registers: [%d, %d, %d, %d]\n", registers[0], registers[1], registers[2], registers[3]);
}

int main() {
	for (int i=0; i<16; i++){
		for (int j=0; j<16; j++){
			opcodes[i][j] = -1;
		}
	}
	int offset = run_examples();
	printf("Operations that behave like 3 or more: %d\n", misbehavers);
	sol2(offset);
	return 0;
}
