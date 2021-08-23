terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

#######################################
resource "docker_image" "nodered_img" {
  name = var.image[terraform.workspace]
}

resource "random_string" "random" {
  count = local.container_count
  length  = 4
  special = false
  upper   = false
}

resource "docker_container" "nodered_container" {
  count = local.container_count
  name  = join("-", ["nodered", terraform.workspace, random_string.random[count.index].result])
  image = docker_image.nodered_img.latest
  ports {
    internal = var.int_port
    
    #####################################################
    external = var.ext_port[terraform.workspace][count.index]
  }
}

