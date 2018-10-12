# Letter-Grade-Calculator
This mini program I created with python calculates and outputs your letter grade when you input your GPA.


def main():
    schoolgrade = input("Enter your GPA: ")
    if schoolgrade >= "3.8":
        print('Grade = A+')
    elif schoolgrade >= "3.4":
        print('Grade = A-')
    elif schoolgrade >= "3.1":
        print('Grade = B+')
    elif schoolgrade >= "2.8":
        print('Grade = B')
    elif schoolgrade >= "2.4":
        print('Grade = B-')
    elif schoolgrade >= "2.1":
        print('Grade = C+')
    elif schoolgrade >= "1.8":
        print('Grade = C')
    elif schoolgrade >= "1.4":
        print('Grade = C-')
    elif schoolgrade >= "1.1":
        print('Grade = D+')
    elif schoolgrade >= "0.6":
        print('Grade = D')
    elif schoolgrade >= "0.0":
        print('Grade = F')
    if schoolgrade >= "":
        main()

    else:
        exit()

main()
