##########################################
variable "image" {
    type = map
    default = {
        dev = "nodered/node-red:latest"
        prod = "nodered/node-red:latest-minimal"
    }
}
###########################################


variable "ext_port" {
  type  = map
  
  validation{
     condition = max(var.ext_port["dev"]...) <= 65500 && min(var.ext_port["dev"]...) >= 1900
     error_message = "The internal port must be 1880 only!!!"
  }
  
  validation{
     condition = max(var.ext_port["prod"]...) <= 1900 && min(var.ext_port["prod"]...) >= 1800
     error_message = "The internal port must be 1880 only!!!"
  }
}

variable "int_port" {
  type    = number
}

locals {
container_count = length(var.ext_port[terraform.workspace])
}