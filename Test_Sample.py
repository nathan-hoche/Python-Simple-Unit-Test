#For Getting actual path
import os
#os.getcwd() -> to get current path
#
import YukiUT

YukiUT.init("Sample", os.getcwd())

YukiUT.check_return("return_value", [], 42)

YukiUT.check_return("return_value", [], 35)

YukiUT.check_return("return_valu", [], 42)
