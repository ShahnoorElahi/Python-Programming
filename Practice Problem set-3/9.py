# 9. Write a Python function that checks whether a passed string is a
#    palindrome or not.



def palindrome(w):
      w1=''
      for i in range(len(w)-1,-1,-1):
        w1+=w[i]
      if w==w1:
          print("It's a palindrome")
      else:
          print("It's not a palindrome",w1)



w=str(input("Enter a String: "))

palindrome(w)


