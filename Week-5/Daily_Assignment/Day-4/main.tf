resource "aws_instance" "myec2" {
  ami           = "ami-00bb6a80f01f03502"
  instance_type = "t2.micro"
  tags = {
    Name = "MyEc2"
  }
}