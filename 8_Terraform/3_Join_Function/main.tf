terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.15.0"
    }
  }
}

provider "docker" {}

# nodered_img is resource name which is utilized in below for making contianer
resource "docker_image" "nodered_img" {
  name = "nodered/node-red:latest"
}

resource "docker_container" "nodered_container" {
  name  = "nodered"

  # nodered_img 
  image = docker_image.nodered_img.latest
  ports {
    internal = 1880
    external = 1880
  }
}

### Focus here
output "IP-Address" {
  value = join (":", [docker_container.nodered_container.ip_address,docker_container.nodered_container.ports[0].external])
  description = "The ip addr & port of container is "
}
