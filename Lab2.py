print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
import statistics 

def display_main_menu():
    print("Display main menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    inputs = input("Enter values: ")
    stringlist = inputs.split(",")
    floatlist = []
    for x in stringlist:
        converted_float = float(x)
        floatlist.append(converted_float)
    
    return floatlist


def calc_average(userinp):
    print("Calculate average")
    length = len(userinp)
    total = 0
    for x in userinp:
        total = total + x

    average = total/length 
    print("Average temperature = " , average)

    return average

    
def find_min_max(userinp):
    print("Find minimum and maximum temperature")
    minimum = min(userinp)
    maximum = max(userinp)
    print("The minimum temperature = " , minimum)
    print("The maximum temperature = " , maximum)

    return minimum, maximum


def sort_temperature():
    print("Sort temperature in ascending order")
    userinp.sort()
    print("Temperature in ascending order = " , userinp)


def calc_median_temperature():
    print("Calculate median temperature")
    median = statistics.median(userinp)
    print("The median temperature is" , median)
 
def main():
    display_main_menu()
    userinp = get_user_input()
    calc_average(userinp)
    find_min_max(userinp)
    sort_temperature()
    calc_median_temperature()

# Will only call functions if program is run directly here, not imported
if __name__=="__main__":
    main()
