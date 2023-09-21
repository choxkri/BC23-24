def NameCheck(name: str):
    if 2 <= len(name) <= 10 and name.isalpha() and name[0:1] == name[0:1].upper():
        return False
    return True


def JobTitleCheck(title: str):
    if len(title) >= 10 and title.replace(" ", "").isalpha():
        return False
    return True


def SalaryCheck(salary: float):
    if 20000.00 <= salary <= 80000.00:
        return False
    return True


def DateCheck(date: str):
    if date[4:5] == "-" and date[7:8] == "-":
        datums = date.split("-")

        year = int(datums[0])
        month = int(datums[1])
        day = int(datums[2])

        if 2022 <= year <= 2023 and 1 <= month <= 12 and 1 <= day <= 31:
            return False
    return True 


def BasicQuestions():
    asking = True
    while asking:
        fn = input("First Name?: ")
        asking = NameCheck(fn)
        if asking:
            print("Input error")
    
    asking = True
    while asking:
        ln = input("Last Name?: ")
        asking = NameCheck(ln)
        if asking:
            print("Input error")
    
    asking = True
    while asking:
        JobTitle = input("Job Title?: ")
        asking = JobTitleCheck(JobTitle)
        if asking:
            print("Input error")

    return [fn, ln, JobTitle]


def JobOffer(info: list):
    asking = True
    while asking:
        salary = input("Annual Salary?: ")
        salary = float(salary.replace(".", "").replace(",", "."))
        asking = SalaryCheck(salary)
        if asking:
            print("Input error")
    
    asking = True
    while asking:
        date = input("Start Date? (YYYY-MM-DD): ")
        asking = DateCheck(date)
        if asking:
            print("Input error")

    email = f"""
Dear {info[0]} {info[1]}, 
 After careful evaluation of your application for the position of {info[2]}, 
 we are glad to offer you the job. Your salary will be {salary} euro annually. 
Your start date will be on {date}. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ
            """
    
    return email

def Rejection(info: list):
    asking = True
    while asking:
        answer = input("Feedback? (Yes or No): ")
        if answer == "Yes" or answer == "No":
            asking = False
        if asking:
            print("Input error")
    
    if answer == "Yes":
        asking = True
        while asking:
            feedback = input("Enter your Feedback (One Statement): ")
            email = f"""
Dear {info[0]} {info[1]}, 
After careful evaluation of your application for the position of {info[2]}, 
at this moment we have decided to proceed with another candidate. 
Here we would like to provide you our feedback about the interview.
{feedback}
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 
                    """
            return email
    
    email = f"""
Dear {info[0]} {info[1]}, 
After careful evaluation of your application for the position of {info[2]}, 
at this moment we have decided to proceed with another candidate.
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
Sincerely, 
HR Department of XYZ 
"""
    return email
        
    

def OfferOrRejection(info: list, option: str):
    if option == "Job Offer":
        print(JobOffer(info))

    elif option == "Rejection":
        print(Rejection(info))

running = True
while running:
    asking = True
    while asking:
        answer = input("More Letters? (Yes or No): ")
        if answer == "Yes" or answer == "No":
            asking = False
        if asking:
            print("Input error")

    if answer == "No":
        quit()

    asking = True
    while asking:
        LetterType = input("Job Offer or Rejection?: ")
        if LetterType == "Job Offer" or LetterType == "Rejection":
            asking = False
        if asking:
            print("Input error")
    
    OfferOrRejection(BasicQuestions(), LetterType)
