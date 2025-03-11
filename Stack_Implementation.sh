max_size=100
top=-1

push() {
    data=$1
    if [ $top -eq $(($max_size - 1)) ]; then
        echo "Overflow: Stack is full."
    else
        top=$((top + 1))
        stack[$top]=$data
        echo "Pushed $data"
    fi
}

pop() {
    if [ $top -eq -1 ]; then
        echo "Underflow: Stack is empty."
    else
        echo "Popped element: ${stack[$top]}"
        top=$((top - 1))
    fi
}

peek() {
    if [ $top -eq -1 ]; then 
        echo "STACK IS EMPTY"
    else
        echo "Top element: ${stack[$top]}"
    fi
}

isEmpty() {
    if [ $top -eq -1 ]; then
        echo "Stack is empty"
    else
        echo "Stack is not empty"
    fi
}

isFull() {
    if [ $top -eq $(($max_size - 1)) ]; then
        echo "Stack is full"
    else
        echo "Stack is not full"
    fi
}

size() {
    echo "Current size of stack: $(($top + 1))"
}

menu() {
    echo "Select an operation:"
    echo "1. Push"
    echo "2. Pop"
    echo "3. Peek"
    echo "4. Check if Stack is Empty"
    echo "5. Check if Stack is Full"
    echo "6. Get Stack Size"
    echo "7. Exit"
}

read -p "Enter the number of operations to perform: " num_operations

for (( i=0; i<$num_operations; i++ ))
do
    menu
    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter data to push: " data
            push $data
            ;;
        2)
            pop
            ;;
        3)
            peek
            ;;
        4)
            isEmpty
            ;;
        5)
            isFull
            ;;
        6)
            size
            ;;
        7)
            echo "Exiting..."
            break
            ;;
        *)
            echo "Invalid choice! Please select a valid option."
            ;;
    esac
done
