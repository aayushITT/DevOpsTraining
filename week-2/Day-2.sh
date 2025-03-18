# Write a shell script to take 2 numbers as input parameter, take user choice to select an arithmetic operation and perform it. The script should be able to handle five basic Arithmetic Operations and print the result based on user choice.

if [ $# -lt 2 ]; then
  echo "Please provide two numbers as parameters."
  echo "Usage: $0 <number1> <number2>"
  exit 1
fi
# echo "Number of parameters : ${#}"
# echo "parameters are : ${@}"
# echo "parameter 1 : $1 and parameter 2 : $2"

num1=$1
num2=$2
if [[ ! "$num1" =~ ^-?[0-9]+$ ]] || [[ ! "$num2" =~ ^-?[0-9]+$ ]]; then
  echo "Both parameters must be valid integers."
  exit 1
fi

echo "OPERATIONS : "
echo "1.Addition"
echo "2.Subtraction"
echo "3.Multiplication"
echo "4.Division"
echo "5.Modulo"

read -p "Enter Your Choice : " choice

case $choice in
1) echo "Addition result : $((num1 + num2)) ";;
2) echo "Subtraction Result : $((num1 - num2))";;
3) echo "Multiplication Result : $((num1 * num2))";;
4)
    if [ $num2 -eq 0 ]; then
      echo "Error: Division by zero is not allowed."
    else
      echo "Division result: $((num1 / num2))"
    fi
    ;;
5)
    if [ $num2 -eq 0 ]; then
      echo "Error: Modulo by zero is not allowed."
    else
      echo "Modulo result: $((num1 % num2))"
    fi
    ;;
*) echo "Invalid choice. Please select a valid operation (1-5)."
esac


