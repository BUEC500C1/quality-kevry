def conversion_func(arabic_num):
    roman_num = ""

    while arabic_num != 0:

        if arabic_num >= 1000:
            times = arabic_num // 1000

            arabic_num = arabic_num - (1000 * times)

            for x in range(int(times)):
                roman_num += 'M'

        elif arabic_num >= 900:
            times = arabic_num // 900

            arabic_num = arabic_num - (900 * times)

            for x in range(int(times)):
                roman_num += 'CM'

        elif arabic_num >= 500:
            times = arabic_num // 500

            arabic_num = arabic_num - (500 * times)

            for x in range(int(times)):
                roman_num += 'D'

        elif arabic_num >= 400:
            times = arabic_num // 400

            arabic_num = arabic_num - (400 * times)

            for x in range(int(times)):
                roman_num += 'CD'

        elif arabic_num >= 100:
            times = arabic_num // 100

            arabic_num = arabic_num - (100 * times)

            for x in range(int(times)):
                roman_num += 'C'

        elif arabic_num >= 90:
            times = arabic_num // 90

            arabic_num = arabic_num - (90 * times)

            for x in range(int(times)):
                roman_num += 'XC'

        elif arabic_num >= 50:
            times = arabic_num // 50

            arabic_num = arabic_num - (50 * times)

            for x in range(int(times)):
                roman_num += 'L'

        elif arabic_num >= 40:
            times = arabic_num // 40

            arabic_num = arabic_num - (40 * times)

            for x in range(int(times)):
                roman_num += 'XL'

        elif arabic_num >= 10:
            times = arabic_num // 10

            arabic_num = arabic_num - (10 * times)

            for x in range(int(times)):
                roman_num += 'X'

        elif arabic_num >= 9:
            times = arabic_num // 9

            arabic_num = arabic_num - (9 * times)

            for x in range(int(times)):
                roman_num += 'IX'

        elif arabic_num >= 5:
            times = arabic_num // 5

            arabic_num = arabic_num - (5 * times)

            for x in range(int(times)):
                roman_num += 'V'

        elif arabic_num >= 4:
            times = arabic_num // 4

            arabic_num = arabic_num - (4 * times)

            for x in range(int(times)):
                roman_num += 'IV'

        elif arabic_num >= 1:
            times = arabic_num // 1

            arabic_num = arabic_num - (1 * times)

            for x in range(int(times)):
                roman_num += 'I'

    return roman_num
