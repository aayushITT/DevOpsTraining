
######
 
$hostname = "16.171.42.68"   
$username = "ec2-user"        
$pemFilePath = "C:\Users\aayush.s\Downloads\myEc2keypair.pem"   
 
 
 
$sshCommand = "ssh -i `"$pemFilePath`" $username@$hostname"

 
Invoke-Expression -Command $sshCommand
