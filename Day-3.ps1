$ExecutionPolicy_choice = Read-Host -Prompt "Choose Execution Policy :`n1:Restricted`n2:AllSigned`n3:RemoteSigned`n4:Unrestricted`n5:Bypass`n6:Undefined"

switch ($ExecutionPolicy_choice) {
    '1' {  
        $ExecutionPolicy = "Restricted"
    }
    '2' {
        $ExecutionPolicy = "AllSigned"
    }
    '3' {
        $ExecutionPolicy = "RemoteSigned"
    }
    '4' {
        $ExecutionPolicy = "Unrestricted"
    }
    '5' {
        $ExecutionPolicy = "Bypass"
    }
    '6' {
        $ExecutionPolicy = "Undefined"
    }
    default {
        Write-Host "Invalid ExecutionPolicy"
        exit 1
    }
}

$ExecutionPolicyScope_choice = Read-Host -Prompt "Choose Execution Policy Scope :`n1:MachinePolicy`n2:UserPolicy`n3:LocalMachine`n4:CurrentUser`n5:Process`n6:Undefined"

switch ($ExecutionPolicyScope_choice) {
    '1' {  
        $Scope = "MachinePolicy"
    }
    '2' {
        $Scope = "UserPolicy"
    }
    '3' {
        $Scope = "LocalMachine"
    }
    '4' {
        $Scope = "CurrentUser"
    }
    '5' {
        $Scope = "Process"
    }
    '6' {
        $Scope = "Undefined"
    }
    default {
        Write-Host "Invalid ExecutionPolicy Scope"
        exit 1
    }
}

# Set the Execution Policy with the chosen values
try {
    Set-ExecutionPolicy $ExecutionPolicy -Scope $Scope
    Write-Host "Execution policy changed to $ExecutionPolicy for scope $Scope!"
} 
catch {
    Write-Host "Error Occurred: $($_.Exception.Message)"
} 
finally {
    Write-Host "Script ran successfully"
}
