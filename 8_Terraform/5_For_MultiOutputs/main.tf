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
  count = 4  
  length = 4
  special = false
  upper = false
}

resource "docker_container" "nodered_container" {
  count = 4
  name  = join("-", ["nodered", random_string.random[count.index].result])
  image = docker_image.nodered_img.latest
  ports {
    internal = 1880
    # we need to mark external ip comment so docker choose random ip
    #external = 1880
  }
}


##################################################################
output "Container-Style1" {
  value = [for i in docker_container.nodered_container[*]:  join(" | ", [i.name, i.ip_address, i.ports[0]["external"] ] )     ] 
  description = "The Name of container is "
}

output "Container-Style2" {
  value = [for i in docker_container.nodered_container[*]:  join(" | ", [i.name, i.ip_address, i.ports[0].external ] )     ] 
  description = "The Name of container is "
}