variable "ext_port" {
  type  = number
}

variable "int_port" {
  type    = number
  validation{
    condition = var.int_port == 1880
    error_message = "The internal port must be 1880 only!!!"
  }
}

variable "counte" {
  type    = number
  default = 1
}
