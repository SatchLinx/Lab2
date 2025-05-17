import statistics
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
     print("Enter some number separated by commas(e.g. 5, 67, 32)")

def calc_average(temperature):
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
def Calculate_Median(temperature):
     x = statistics.median(temperature)
     return x


     

    

def main():
    display_main_menu()
    temperature = get_user_input()
    asc_ord = sort_temperature(temperature)
    average = calc_average(temperature)
    min_max = find_min_max(temperature)
    median = Calculate_Median(temperature)
    print(str(asc_ord))
    print("Average = " + str(average))
    print("Median = " + str(median))
    print("min,max = " + str(min_max))
    
   
 


if __name__ == "__main__":
    main()

