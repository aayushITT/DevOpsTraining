variable "tf-demo-s3-bucket" {
  default     = "my-terraform-state-bucket-weekly-assignment"
  type        = string
  description = "S3 bucket used for storing state file in remote backend."
}