def arithmetic_arranger(problems, solve = False):
    line_1 = []
    line_2 = []      
    line_3 = []
    line_4 = []

    if (len(problems) > 5) :
      return "Error: Too many problems."
      
    for problem in problems:
        problem = problem.replace(" ", "")
        if "+" in problem:
            separator = "+"
        elif "-" in problem: 
            separator = "-"
        else: 
            return "Error: Operator must be '+' or '-'."
        
        first, second = problem.split(separator) 

        len_first = len(first)
        len_second = len(second)
        len_line = max(len_first, len_second) + 2
        space_first = len_line - len_first
        space_second = len_line - len_second - 1

        if (len(first) >=5 or len(second)>=5):
            return "Error: Numbers cannot be more than four digits."
          
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
            
        if separator == "+":
            total = int(first) + int(second)
        else: 
            total = int(first) - int(second)
        
        len_total = len(str(total)) 
        space_total = len_line - len_total
      
        str_1 = " " * space_first + first  
        str_2 = separator + " " * space_second + second
        str_3 = "-" * len_line
        str_4 = " " * space_total + str(total)
        line_1.append(str_1)
        line_2.append(str_2)
        line_3.append(str_3)
        line_4.append(str_4)    

    final_1 = "    ".join(line_1)
    final_2 = "    ".join(line_2)
    final_3 = "    ".join(line_3)
    final_4 = "    ".join(line_4)   
    if solve:
        arranged_problems = final_1 + "\n" + final_2 + "\n" + final_3 + "\n" + final_4
    else:  
        arranged_problems = final_1 + "\n" + final_2 + "\n" + final_3
    return arranged_problems
  
