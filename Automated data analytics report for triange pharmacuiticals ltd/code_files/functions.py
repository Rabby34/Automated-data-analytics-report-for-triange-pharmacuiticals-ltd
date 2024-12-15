def convert(number):
    number = number/10000000
    number = round(number,1)
    number = format(number,',')
    number = number + ' Cr'
    return number

def percentage(sales,target):
    number = (sales/ target)*100
    number = round(number, 1)
    number = str(number) + ' %'
    return number

def convert_small_amount(number):
    number = int(number/1000)
    number = format(number,',')
    number = number + ' K'
    return number