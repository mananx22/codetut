terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

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

