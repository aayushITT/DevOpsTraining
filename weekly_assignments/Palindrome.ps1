function Test-Palindrome {
    param (
        [Parameter(Mandatory)]
        [int]$Number
    )
    
    if ($Number -lt 0) {
        Write-Output "The Number $Number is not a Palindrome (negative numbers)."
        return
    }
    
    $originalNumber = $Number
    $reversedNumber = 0

    while ($Number -gt 0) {
        $remainder = $Number % 10
        $reversedNumber = ($reversedNumber * 10) + $remainder
        $Number = [int]($Number / 10)
    }

    if ($reversedNumber -eq $originalNumber) {
        Write-Output "The Number $originalNumber is a Palindrome."
    } else {
        Write-Output "The Number $originalNumber is not a Palindrome."
    }
}

try {
    $num = Read-Host -Prompt "Enter a Number"

    if ($num -match '^\d+$') {
        Test-Palindrome -Number $num
    } else {
        Write-Output "Invalid input! Please enter a valid number."
    }
}
catch {
    Write-Output "An error occurred: $($_.Exception.Message)"
}
