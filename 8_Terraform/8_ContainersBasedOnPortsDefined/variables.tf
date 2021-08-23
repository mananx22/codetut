variable "ext_port" {
  type  = list
  
  ###########################
   validation{
     condition = max(var.ext_port...) <= 65500 && min(var.ext_port...) >= 1000
     error_message = "The internal port must be 1880 only!!!"
  }
}

variable "int_port" {
  type    = number
}



locals {
container_count = length(var.ext_port)
}