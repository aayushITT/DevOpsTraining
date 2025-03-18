check_prime() {
    local number=$1

    if [ $number -le 1 ]; then
        echo "Not a Prime Number"
        return 1
    fi

    for ((i=2; i*i<=number; i++)); do
        if [ $((number % i)) -eq 0 ]; then
            echo "Not a Prime Number"
            return 1
        fi
    done

    echo "It is a Prime Number"
}

read -p "Enter Number To Be Checked: " num
check_prime $num
