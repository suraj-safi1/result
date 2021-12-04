Name=input("Student Name:")
Rollno=int(input("enter rollno:"))
Maths=float(input("Enter your maths marks:"))
English=float(input("Enter your english marks:"))
Hindi=float(input("Enter your hindi marks:"))
Science=float(input("Enter your science marks:"))
Ssci=float(input("Enter your Ssci marks:"))
Total=Maths+English+Hindi+Science+Ssci
print("Student Name",Name,"Total marks",Total)
percentage=(Total/5)
print("Percentage",percentage)
if Total >= 165 and English >= 33 and Hindi >= 33 and Science >= 33 and Maths >= 33 and Ssci >= 33:
    if Total > 164 and Total < 300:
     print(" Congrats You are Passed")
    elif Total >=300 and Total < 350 :
            print(" cONTRAGTS first class")
    elif Total >= 350:
                print("PASSED WITH Distinction")
else:
    print('You are Fail')
                    