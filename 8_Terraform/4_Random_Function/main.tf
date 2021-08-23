terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

#focus here
resource "random_string" "random" {
  length = 4
  special = false
  upper = false
}

resource "docker_image" "nodered_img" {
  name = "nodered/node-red:latest"
}

resource "docker_container" "nodered_container" {
  name  = join("-", ["nodered", random_string.random.result])
  image = docker_image.nodered_img.latest
  ports {
    internal = 1880
    external = 1880
  }
}

output "Container" {
  value = join(" | ", [docker_container.nodered_container.name, docker_container.nodered_container.ip_address, docker_container.nodered_container.ports[0].external]) 
  description = "The Name of container is "
}