# 10. Write a program that displays ―Kamran Akmal‖ on output, if score >30, Shoaib Akhtar,
#     if 20<score <30, and Shahid Afridi if 10<score <20.


score=int(input('Enter score: '))
if score > 30:
        print("Kamran Akmal")
elif 20<score <30:
        print("Shoaib Akhtar,")
elif 10<score < 20:
        print("Shahid Afridi")
else:
        print("Out of range")
