import statistics
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
     print("Enter some number separated by commas(e.g. 5, 67, 32)")

def calc_average(temperature):
     print("calc_average")
     total = sum(temperature)
     n = len(temperature)
     A = total/n
     return A



def get_user_input():
     x = input()
     text = x.split(",")
     print(text)
     thislist = list(map(float,text))
     print(thislist)
     return thislist

def find_min_max(temperature):
     maxvalue = max(temperature)
     minvalue = min(temperature)
     maxmin = [minvalue,maxvalue]
     return maxmin
def sort_temperature(temperature):
     temperature.sort()
     return temperature
def calc_median_temperature(temperature):
     median_value = statistics.median(temperature)
     return median_value
     

    

def main():
    display_main_menu()
    temperature = get_user_input()
    asc_ord = sort_temperature(temperature)
    average = calc_average(temperature)
    median = calc_median_temperature(temperature)
    min_max = find_min_max(temperature)
    print("Average = " + str(average))
    print("median = " + str(median))
    print("min,max = " + str(min_max))
    print("This is the numbers in ascending order: " + str(asc_ord))
 


if __name__ == "__main__":
    main()


