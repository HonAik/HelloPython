
# all affects the function u want to import, not neccesary
__all__ = ["outline","NAME"]


NUM = 123
NAME = "Reynolds"

def outline():
    print('!' * 10) # means print ! 10 times 

# outline(),if u want to import but here some print make u crazy, use __name__, 
# in this file, the value of __name__ is '__main__'
# but in other files, the value of this __name__ = the file name
# therefor if you want the call only in current file and dont want in other file then use this:

if __name__ == '__main__':
    outline()
