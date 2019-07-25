# Letter-Grade-Calculator using python.
This program I created calculates and output your letter grade when you input your GPA.
This program was created using python.

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



# if client enters blank, echo "enter your GPA
# if client enter non int, echo "enter numbers only"
