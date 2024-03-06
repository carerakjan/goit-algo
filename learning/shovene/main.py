import random
import statistics as st


def generate(amount: int):
    num = []
    mu = 100
    sigma = 50
    for i in range(amount):
        num.append(random.gauss(mu, sigma))
    return num


def get_coefficients():
    crits = {}
    with open('./shovene_coefs.txt', 'r') as fh:
        lines = fh.readlines()
        for l in [l.strip() for l in lines]:
            n, m, *_ = l.split(',')
            crits[int(n)] = float(m)
    return crits


def main():
    data = generate(30)
    data_sorted = sorted(data)
    sh_crits = get_coefficients()
    count = 1

    while True:
        data_len = len(data_sorted)
        data_mean = st.mean(data_sorted)
        data_stdev = st.stdev(data_sorted)
        data_max = max(data_sorted)
        data_min = min(data_sorted)

        sh_min = (data_mean - data_min) / data_stdev
        sh_max = (data_max - data_mean) / data_stdev
        sh_crit = sh_crits[data_len]

        print(f'-------- ітерація - {count} -----------')
        print('дані: ', data_sorted)
        print('кількість даних: ', data_len)
        print('середнє арифметичне: ', data_mean)
        print('стандартне відхилення: ', data_stdev)
        print('мінімільне значення: ', data_min)
        print('максимальне значення: ', data_max)
        print(f'критичне значення Шовене: ', sh_crit)
        print('коеф. Шовене для мін. значення: ', sh_min)
        print('коеф. Шовене для макс. значення: ', sh_max)

        count += 1
        misses = 0

        if sh_min >= sh_crit:
            print(f'мінімільне значення "{data_min}" є промахом')
            data_sorted = data_sorted[1:]
            misses += 1

        if sh_max >= sh_crit:
            print(f'максимальне значення "{data_max}" є промахом')
            data_sorted = data_sorted[:-1]
            misses += 1

        if misses > 0:
            continue

        print('промахів не має')
        break


if __name__ == '__main__':
    main()
