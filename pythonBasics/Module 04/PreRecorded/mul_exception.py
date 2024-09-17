

try:
    with open("new.text", "r") as file:
        content = file.read()
        result = 10/int(content)
        print(result)

except Exception as e:
        print(e)
""" 
except FileNotFoundError:
    print("File Not Found")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
"""
