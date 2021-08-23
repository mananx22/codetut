terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

#############################################
variable "ext_port" {
  type    = number
  default = 1880
}

variable "int_port" {
  type    = number
  
     ######
  default = 1881
  validation{
    condition = var.int_port == 1880
    error_message = "The internal port must be 1880 only!!!"
     ######
     
  }
}

variable "counte" {
  type    = number
  default = 1
}
#############################################



resource "docker_image" "nodered_img" {
  name = "nodered/node-red:latest"
}

resource "random_string" "random" {

  count = var.counte

  length  = 4
  special = false
  upper   = false
}

resource "docker_container" "nodered_container" {
  count = var.counte
  name  = join("-", ["nodered", random_string.random[count.index].result])
  image = docker_image.nodered_img.latest
  ports {
    internal = var.int_port
    # we need to mark external ip comment so docker choose random ip
    external = var.ext_port
  }
}

output "Container-Style1" {
  value       = [for i in docker_container.nodered_container[*] : join(" | ", [i.name, i.ip_address, i.ports[0]["external"]])]
  description = "The Name of container is "
}

output "Container-Style2" {
  value       = [for i in docker_container.nodered_container[*] : join(" | ", [i.name, i.ip_address, i.ports[0].external])]
  description = "The Name of container is "
}