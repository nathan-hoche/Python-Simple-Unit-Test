#For Getting actual path
import os
#os.getcwd() -> to get current path
#
import YukiUT

YukiUT.init("Sample", os.getcwd())

print("Return 42: ")
YukiUT.check_return("return_42", [], 42)
YukiUT.check_return("return_42", [], 35)
YukiUT.check_return("return_999", [], 42)

print("\nReturn value: ")
YukiUT.check_return("return_value", [3], 3)
YukiUT.check_return("return_value", [""], 3)
YukiUT.check_return("return_value", [3, 3], 3)