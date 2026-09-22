# 1. Write a PYTHON program to evaluate the student performance

#     If % is >=90 then Excellent performance

#     If % is >=80 then  Very Good performance

#     If % is >=70 then Good performance

#     If % is >=60 then average performance

performance = int(input("Masukkan nilai performa: "))
if performance >= 90:
    print("Excellent performance")
elif performance >= 80:
    print("Very Good performance")
elif performance >= 70:
    print("Good performance")
elif performance >= 60:
    print("Average performance")
else:
    print("Poor performance")