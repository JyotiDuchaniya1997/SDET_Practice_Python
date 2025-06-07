str="ADHBCOIEgyufdgHJSGFDJDFbnBVCDEmDCV"

case=input("enter the case in which it should be converted to: ")
# Uisng In built functaions
if case.lower()=='l':
    str1 = str.lower()
elif case.lower()=='u':
    str1= str.upper()

print(f"Case converted is {str1}")
