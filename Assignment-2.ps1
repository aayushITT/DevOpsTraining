$ModuleName = Read-Host -Prompt "Enter the name of the module you want to install"

try {
    Install-Module -Name $ModuleName -Force -Scope CurrentUser 
    Write-Host "Module $ModuleName installed successfully."
}
catch {
    Write-Host "Error installing module: $($_.Exception.Message)"
}

try {
    Import-Module -Name $ModuleName
    Write-Host "Module $ModuleName imported successfully."
}
catch {
    Write-Host "Error importing module: $($_.Exception.Message)"
}

try {
    $ModuleCommands = Get-Command -Module $ModuleName
    Write-Host "Commands available in module $ModuleName :"
    $ModuleCommands | ForEach-Object { Write-Host $_.Name }
}
catch {
    Write-Host "Error retrieving commands for module: $($_.Exception.Message)"
}
