
try:
    with open("new.text", "r") as file:
        content = file.read()
        result = 10/int(content)
        print(result)

except Exception as e:
        print(e)

finally:
    print("Execution Completed")
