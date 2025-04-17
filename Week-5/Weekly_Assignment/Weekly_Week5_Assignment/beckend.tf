terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket-weekly-assignment"
    key    = "terraform.tfstate"
    region = "ap-south-1"

  }
}
 