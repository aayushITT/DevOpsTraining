module "s3" {
  source = "./modules/s3"
}
module "ec2" {
  source = "./modules/ec2"
}

 output "public_ip_address" {
  value = module.ec2.public-ipv4-address
}