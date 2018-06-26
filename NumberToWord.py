# number to words. Example: 1576, output is: one thousand, five hundred seventy six
num=int(input('please enter an integer between 1 and 9999: '))

def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty', \
          30 : 'thirty', 40 : 'fourth', 50 : 'fifty', 60 : 'sixty', \
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    k = 1000
    t = k * 1000

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred ' + int_to_en(num % 100)
    if (num < t):
        if num % k == 0:
            return int_to_en(num // k) + ' thousand'
        else:
            return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

print int_to_en(num)