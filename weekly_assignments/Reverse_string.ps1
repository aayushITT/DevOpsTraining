function Reverse-String {
    param (
        [Parameter(Mandatory=$true)]
        [string]$inputString
    )
    
    if ([string]::IsNullOrEmpty($inputString)) {
        Write-Host "Error: Input string cannot be empty or null."
        return
    }

    $reversedString = ""

    for ($i = $inputString.Length - 1; $i -ge 0; $i--) {
        $reversedString += $inputString[$i]
    }

    Write-Host "Reversed String: $reversedString"
}

$userInput = Read-Host -Prompt "Enter a string to reverse"
Reverse-String -inputString $userInput
