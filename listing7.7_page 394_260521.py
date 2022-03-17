def main():
    NUM_WORK = 6 # number of workers
    work_hrs = []
    count = 0
    PAY = 30
    for i in range(NUM_WORK):
        count += 1
        hours = int(input('Enter number of hours overworked for the worker nr' + str(count) + ':'))
        while hours > 84: #GIGO - garbage in/garbage out
            print()
            print('Max number of working hours in the week is 84!')
            hours = int(input('Enter correct number of hours overworked during the week:'))

        work_hrs.append(hours)
    print('List of overworked hours for 6 workers is:', work_hrs)
    pay_list = []
    count2 = 0
    for hr in work_hrs:
        gross_pay = hr * PAY
        count2 +=1
        print('Gross pay for worker nr', count2,'is:',gross_pay)
        pay_list.append(gross_pay)
    print('Pay list for 6 workers is:',pay_list)




main()