output "public-ipv4-address" {
  value = aws_instance.myec2.public_ip
}