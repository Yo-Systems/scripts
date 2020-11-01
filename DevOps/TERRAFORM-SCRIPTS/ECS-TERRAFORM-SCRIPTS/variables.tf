
variable "region" {
    description = "The AWS region to create resources in."
    default = "us-west-2"
}


variable "availability_zone" {
    description = "The availability zone"
    default = "us-west-2a, us-west-2b"
}

variable "ecs_cluster_name" {
    description = "The name of the Amazon ECS cluster."
    default = "yo-systems-cluster"
}

variable "amis" {
    description = "Which AMI to spawn. Defaults to the AWS ECS optimized images."
   
    default = {
        us-west-2 = "ami-92e06fea"
    }
}


variable "autoscale_min" {
    default = "1"
    description = "Minimum autoscale (number of EC2)"
}

variable "autoscale_max" {
    default = "2"
    description = "Maximum autoscale (number of EC2)"
}

variable "autoscale_desired" {
    default = "1"
    description = "Desired autoscale (number of EC2)"
}


variable "instance_type" {
    default = "t2.micro"
}

variable "ssh_pubkey_file" {
    description = "Path to an SSH public key"
    default = "id_rsa.pub"
}