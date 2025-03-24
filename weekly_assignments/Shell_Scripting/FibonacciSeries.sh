
Generate_Fibonacci_Series()
{
    num=$1
    if [ $num -le 0 ]
    then
    echo "Please Enter Number Greater the 0 "
    return 1

    else
    a=0
    b=1
    for((i=0;i<$num;i++))
    do
    echo -n "$a "
    c=$((a + b))
    a=$b
    b=$c

    done

    fi 


}

read -p "Enter how many numbers of fibonacci series to be generated : " num 
Generate_Fibonacci_Series $num
