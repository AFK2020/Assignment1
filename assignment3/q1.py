

def extract_number_sum(string):
    sum=0

    try:
        for char in string:
            if char.isdigit():
                sum=sum+int(char)
        
        return sum
    except:
        print("Some unexpected error occured")


str1=input("Enter string")

print(extract_number_sum(str1))