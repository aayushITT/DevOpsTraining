try {
    $inputYear = Read-Host -Prompt "Enter year: "

    if (-not ($inputYear -as [int])) {
        throw "The input is not a valid year. Please enter a numeric value."
    }

    $inputYear = [int]$inputYear

    if ($inputYear -le 0) {
        throw "The year must be a positive integer."
    }

    if ($inputYear % 4 -eq 0 -and ($inputYear % 100 -ne 0 -or $inputYear % 400 -eq 0)) {
        Write-Host "$inputYear is a Leap Year!"
    } else {
        Write-Host "$inputYear is not a Leap Year."
    }
}
catch {
    Write-Host "Error: $($_.Exception.Message)"
}
