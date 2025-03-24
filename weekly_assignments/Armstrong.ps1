$num = Read-Host -Prompt "Enter a Number"
$num = [int]$num  

 
$snum = $num.ToString()
$digits = $snum.Length

$temp = $num
$res = 0

Write-Host "Digits in number: $digits"
Write-Host "Original number: $num"
 
while ($temp -gt 0) {
    $rem = $temp % 10
    Write-Host "Remainder: $rem"
    $res += [Math]::Pow($rem, $digits)
    Write-Host "Current sum: $res"
    $temp = [int]($temp / 10)
}

 
if ($num -eq $res) {
    Write-Host "$num is an Armstrong number"
} else {
    Write-Host "$num is not an Armstrong number"
}
