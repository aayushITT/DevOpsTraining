read -p "Enter size of array: " size
# echo $size
echo "Enter array elements : "
i=0
while [ $i -lt $size ]
do
read -p "Enter array element $((i+1)) : " array[$i]
let i++
done

# echo "${array[*]}"

echo "Alternating   Elements Are: "
for((i=0;i<$size;i=i+2))
do
echo " ${array[$i]}"
done