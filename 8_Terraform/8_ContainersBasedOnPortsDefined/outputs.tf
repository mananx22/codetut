output "Container-Style1" {
  value       = [for i in docker_container.nodered_container[*] : join(" | ", [i.name, i.ip_address, i.ports[0]["external"]])]
  description = "The Name of container is "
}

output "Container-Style2" {
  value       = [for i in docker_container.nodered_container[*] : join(" | ", [i.name, i.ip_address, i.ports[0].external])]
  description = "The Name of container is "
} 