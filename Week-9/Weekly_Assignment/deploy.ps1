$resourceGroupName = "myDemoRG"
$location = "eastus"
$templateFile = "azuredeploy.json"
$adminUsername = "azureuser"
$sshPublicKeyPath = "C:\Users\aayush.s\.ssh\id_ed25519.pub"


$sshPublicKey = Get-Content -Raw -Path $sshPublicKeyPath

Write-Host "Connecting azure account"
Connect-AzAccount -TenantId "f1882fe3-0667-47de-98dc-aaa79f30c9a4"

Write-Host "Ensuring resource group exists..."
New-AzResourceGroup -Name $resourceGroupName -Location $location -Verbose

Write-Host "Deploying ARM template..."
New-AzResourceGroupDeployment `
    -ResourceGroupName $resourceGroupName `
    -TemplateFile $templateFile `
    -adminUsername $adminUsername `
    -adminPublicKey $sshPublicKey `
    -Verbose