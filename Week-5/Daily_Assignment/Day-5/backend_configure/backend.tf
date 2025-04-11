terraform {
  backend "s3" {
    bucket = "b-0000001"
    key = "~/terraformPractice/AWS-practice/backend_configure/terraform.tfstate"
    region = "ap-south-1"

  }
}