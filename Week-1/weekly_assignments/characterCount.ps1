function CountCharacterOccurrences {
    param (
        [Parameter(Mandatory=$true)]
        [string]$inputString
    )
    
    if ([string]::IsNullOrEmpty($inputString)) {
        Write-Host "Error: Input string cannot be empty or null."
        return
    }

    $characterCount = @{}

    foreach ($character in $inputString.ToCharArray()) {
        if ($characterCount.ContainsKey($character)) {
            $characterCount[$character]++
        } else {
            $characterCount[$character] = 1
        }
    }

    $characterCount.GetEnumerator() | ForEach-Object { Write-Host "$($_.Key): $($_.Value)" }
}

$userInputString = Read-Host -Prompt "Enter a string to count character occurrences"
CountCharacterOccurrences -inputString $userInputString
