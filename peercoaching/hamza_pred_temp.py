more_letters = input("Yes or No: ")
if more_letters == 'No' or more_letters == 'no':
    print("Input error")
    quit()
elif more_letters == 'Yes' or more_letters == 'yes':
    job_offer = input("Job Offer or Rejection?: ")
    if job_offer == 'Job Offer':
        first_name = input("First Name: ")
        while len(first_name) < 2 or len(first_name) > 10 or first_name[0].islower():
            print("Input error")
            first_name = input("First Name: ")
        last_name = input("Last Name: ")
        while len(last_name) < 2 or len(last_name) > 10 or last_name[0].islower():
            print("Input error")
            last_name = input("Last Name: ")
        job_title = input("Job Title: ")
        while len(job_title) < 10 or job_title.isnumeric():
            print("Input error")
            job_title = input("Job Title: ")
        annual_salary = input("Annual salary:")
        while (annual_salary.__contains__(',')) or float(annual_salary) < 20000.00 or float(annual_salary) > 80000.00:
            print("Input error")
            annual_salary = input("Annual salary:")
        start_date = input("Start Date (YYYY-MM-DD): ")
        while int(start_date[0:4]) < 2021 or int(start_date[0:4]) > 2022 or int(start_date[5:7]) < 1 or int(
                start_date[5:7]) > 12 or int(start_date[8:10]) < 1 or int(start_date[8:10]) > 31:
            print("Input Error")
            start_date = input("Starting date with format (YYYY-MM-DD):")
        print(
            f"Here is the final letter to send: Dear {first_name}-{last_name}, After careful evaluation of your application for the position of {job_title}, we are glad to offer you the job. Your salary will be {annual_salary} euro annually. Your start date will be on {start_date}. Please do not hesitate to contact us with any questions. Sincerely, HR Department of XYZ")

    elif job_offer == 'Rejection':
        first_name = input("First Name: ")
        while len(first_name) < 2 or len(first_name) > 10 or first_name[0].islower():
            print("Input error")
            first_name = input("First Name: ")
        last_name = input("Last Name: ")
        while len(last_name) < 2 or len(last_name) > 10 or last_name[0].islower():
            print("Input error")
            last_name = input("Last Name: ")
        job_title = input("Job Title: ")
        while len(job_title) < 10 or job_title.isnumeric():
            print("Input error")
            job_title = input("Job Title: ")