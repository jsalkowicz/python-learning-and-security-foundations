try:
    print(32 / 0)
except ZeroDivisionError as error:
    print(error)
finally:
    print("This part always runs")
