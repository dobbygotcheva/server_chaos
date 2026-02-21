variable "region" {
  type        = string
  description = "AWS region for deployment"
  default     = "us-east-1"
}

variable "cluster_name" {
  type        = string
  default     = "cloud-native"
}

variable "vpc_cidr" {
  type        = string
  default     = "10.10.0.0/16"
}

variable "azs" {
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "public_subnets" {
  type        = list(string)
  default     = ["10.10.1.0/24", "10.10.2.0/24", "10.10.3.0/24"]
}

variable "private_subnets" {
  type        = list(string)
  default     = ["10.10.11.0/24", "10.10.12.0/24", "10.10.13.0/24"]
}
