import random
import statistics as st
import re
import sys

def get_data():
    try:
        with open('./da5ta.txt', 'r') as fh:
            lines = fh.readlines()
            return list(map(lambda str: float(str.replace(',', '.')),[line.strip() for line in lines if line.strip()]))
    except Exception:
        return []

def generate(amount: int):
    num = []
    mu = 100
    sigma = 50
    for i in range(amount):
        num.append(round(random.gauss(mu, sigma), 3))
    return num

def parse_coefs(lines, coefs):
    for line in [lst.split() for lst in lines if re.search('[^a-z]+', (''.join(lst.split())).lower())]:
        for idx, item in enumerate(line):
            if (idx % 2 == 0):
                z = float(item)
                m = int(line[idx + 1])
                coefs[z] = m

def get_coefficients():
    coefs = {}
    with open('./shovene_coefs.txt', 'r') as fh:
        lines = fh.readlines()
        parse_coefs(lines, coefs)

    return dict(sorted(coefs.items()))


def check_miss(val_coef, val_nums, coefs):
    for coef in coefs.keys():
        if (val_coef <= coef):
            return val_nums < coefs[coef]
        


def main():
    data = map(float, sys.argv[1:]) if len(sys.argv) > 1 else (get_data() or generate(30))
    data_sorted = sorted(list(data))
    sh_coefs = get_coefficients()
    count = 1

    while True:
        data_len = len(data_sorted)
        data_mean = st.mean(data_sorted)
        data_stdev = st.stdev(data_sorted, data_mean)
        data_max = max(data_sorted)
        data_min = min(data_sorted)

        sh_min = (data_mean - data_min) / data_stdev
        sh_max = (data_max - data_mean) / data_stdev

        print(f'-------- ітерація - {count} -----------')
        print('дані: ', data_sorted)
        print('кількість даних: ', data_len)
        print('середнє арифметичне: ', data_mean)
        print('стандартне відхилення: ', data_stdev)
        print('мінімільне значення: ', data_min)
        print('максимальне значення: ', data_max)
        print('коеф. Шовене для мін. значення: ', sh_min)
        print('коеф. Шовене для макс. значення: ', sh_max)

        count += 1
        misses = 0

        if check_miss(sh_min, data_len, sh_coefs):
            print(f'мінімільне значення "{data_min}" є промахом')
            data_sorted = data_sorted[1:]
            misses += 1

        if check_miss(sh_max, data_len, sh_coefs):
            print(f'максимальне значення "{data_max}" є промахом')
            data_sorted = data_sorted[:-1]
            misses += 1

        if misses > 0:
            continue

        print('промахів не має')
        break


if __name__ == '__main__':
    main()
