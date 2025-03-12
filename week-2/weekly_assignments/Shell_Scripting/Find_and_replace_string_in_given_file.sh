Replace_String_In_Given_File()
{
    file=$1
    string=$2
    replacewith=$3

    if [ ! -f $file ]; then
        echo "File does not exist"
        return
    else
        echo "Before replacing:"
        cat $file
        echo

        sed -i "s/$string/$replacewith/g" $file

        echo "After replacing:"
        cat $file
         echo
    fi
}

read -p "Enter file name: " file
read -p "Enter string to be replaced: " string
read -p "Enter replaced string: " replacedstring

Replace_String_In_Given_File $file $string $replacedstring
