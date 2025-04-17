 resource "aws_instance" "myec2" {
  ami           = "ami-000b013aed8dfda72"  
  instance_type = "t2.micro"              

  tags = {
    Name = "MyEc2"

  }
}
resource "aws_s3_bucket" "b-0000001" {
  bucket = "b-0000001"
}