import sys
import random
import string

MIN_LINES = 5
MAX_LINES = 100

MIN_LEN = 10
MAX_LEN = 100

ROMEO_OCCURANCE = 0.05

def main(num_samples=1, num_lines=-1):
    if num_lines == -1:
        gen_num_lines = True
    for i in range(num_samples):
        if gen_num_lines:
            num_lines = random.randint(MIN_LINES, MAX_LINES)
        line_len = random.randint(MIN_LEN, MAX_LEN)
        with open('samples/input/input' + str(i) + '.txt', 'w') as f:
            f.write(str(num_lines) + ' ' + str(line_len) + '\n')
            
            for _ in range(num_lines):
                romeo_insert_loc = random.randint(0, int(line_len / 0.1)) 
                j = 0
                while j < line_len:
                    if romeo_insert_loc < line_len - len('Romeo') and \
                            j == romeo_insert_loc:
                        f.write('Romeo')
                        j += len('Romeo')
                    else:
                        f.write(random.choice(string.ascii_letters))
                        j += 1
                f.write('\n')




def check_args():
    num_samples = int(sys.argv[1])
    assert num_samples >= 1, 'Number of samples must be at least 1'

    if len(sys.argv) > 2:
        num_lines = int(sys.argv[2])
        assert int(num_lines) >= MIN_LINES and int(num_lines) <= MAX_LINES, \
            'Invalid number of lines, must be between ' + MIN_LINES + ' and ' \
                    + MAX_LINES
        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        check_args()
        main(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        check_args()
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        main()

