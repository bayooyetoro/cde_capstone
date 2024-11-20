terraform {
  backend "remote" {
    organization = "DataByte_Analytica"
    workspaces {
      name = "DataByte"
    }    
  }
  
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.76.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_data_bucket" {
  bucket = "cde-raw-data"
}