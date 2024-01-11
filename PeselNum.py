PESEL_LENGTH = 11
PESEL_WEIGHT = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
## validation the date
def is_valid_date(year, month, day):
    if 81 <= month <= 92:
           year += 1800
           month -= 80
    elif 1 <= month <= 12:
            year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    return 0 <= year <= 2299 and 1 <= month <= 12 and 1 <= day <= 31

# counters
total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0

file = open("1e6.dat", 'r')

# main processing loop
for pesel in file:
    pesel=pesel.strip()
    total += 1
    if not (len(pesel)==PESEL_LENGTH):
        invalid_length += 1
    elif not (pesel.isdigit()):
        invalid_digit += 1
    elif not ( is_valid_date(int(pesel[0:2]),int(pesel[2:4]), int(pesel[4:6])) ):
        invalid_date += 1
    else:
            checksum = 0
            for i in range(PESEL_LENGTH - 1):
                checksum += PESEL_WEIGHT[i] * int(pesel[i])
            checksum = (10 - (checksum % 10)) % 10
            if  (checksum != int(pesel[10])):
                    invalid_checksum += 1
            else:
                 correct += 1
                 if (int(  pesel[-2]) % 2 ==0 ):
                         female += 1
                 else : 
                            male += 1

file.close()


# show results
print(total, correct, female, male)
print(invalid_length, invalid_digit, invalid_date, invalid_checksum)