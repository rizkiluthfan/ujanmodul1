def create_phone_number(number):
    phone_number = '('
    for i, num in enumerate(number):
        if i < 3:
            phone_number += str(num)
            if i == 2:
                phone_number += ') '
        elif i <= 13:
            phone_number += str(num)
            if i == 5:
                phone_number += '-'
    return phone_number
print (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) 