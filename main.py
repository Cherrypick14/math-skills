import sys

from data_utils import (
   read_data,
   calculate_average,
   calculate_median,
   calculate_variance,
   calculate_standard_deviation
)

# Entry of the program
if __name__ == "__main__":
   if len(sys.argv) != 2 :
      print("Usage: python3 main.py <data_file_path>")
      sys.exit(1)
   file_path = sys.argv[1]
   
   data = read_data(file_path)
   average = calculate_average(data)
   median = calculate_median(data)
   variance = calculate_variance(data)
   standard_deviation = calculate_standard_deviation(data)

   print(f"Average: {round(average)}")
   print(f"Median : {round(median)}")
   print(f"Variance: {round(variance)}")
   print(f"Standard Deviation: {round(standard_deviation)}")
 

  
   
   