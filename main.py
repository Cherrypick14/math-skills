import os
import sys
import math

def read_data(file_path):
    try:
        if not os.path.exists(file_path):
         raise FileNotFoundError("f Error: The file {file_path} doesn't exist")
        
        if os.path.getsize(file_path) == 0:
           raise ValueError("f Error: The file {file_path} is empty}")
        
        with open(file_path,'r') as file:
            data = [int(line.strip()) for line in file]
           
        return data 
    except FileNotFoundError as fnf_error:
       print(fnf_error)
       sys.exit(1)
    except ValueError as val_error:
       print(val_error)
       sys.exit(1)
    except Exception as e:
       print(f"An unexpected error occurred: {e}")
       sys.exit(1)
    
def calculate_average(data):
   """Calculate and return the average of the data."""
   return sum(data) / len(data)

def calculate_median(data):
   """Calculate and return the median of the data."""
   sorted_data = sorted(data)
   n = len(sorted_data)
   mid = n // 2
   if n % 2 == 0:
      return (sorted_data[mid] + sorted_data[mid - 1]) / 2
   else:
      return sorted_data[mid]
#  finds the average of the data set, then calculates the squared differences of each data point from that average, sums those squared differences, and finally divides the sum by the number of data points to obtain the variance.
def calculate_variance(data):
    average = calculate_average(data)
   # variance = Σ(x - μ)^2 / N
    return sum((x - average) ** 2 for x in data) / len(data)

def calculate_standard_deviation(data):
   variance = calculate_variance(data)
   return math.sqrt(variance)

def main(file_path):
   data = read_data(file_path)
   average = calculate_average(data)
   median = calculate_median(data)
   variance = calculate_variance(data)
   standard_deviation = calculate_standard_deviation(data)

   print(f"Average: {round(average)}")
   print(f"Median : {round(median)}")
   print(f"Variance: {round(variance)}")
   print(f"Standard Deviation: {round(standard_deviation)}")
   
# Entry of the program
if __name__ == "__main__":
   if len(sys.argv) != 2 :
      print("Usage: python3 main.py <data_file_path>")
      sys.exit(1)

   file_path = sys.argv[1]
   main(file_path)
   