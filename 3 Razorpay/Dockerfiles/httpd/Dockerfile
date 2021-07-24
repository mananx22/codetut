FROM php:8.0.7-apache
# COPY run.sh /var/www/html/
# RUN  chmod u+x,g+x /var/www/html/run.sh
#RUN apt update 
#RUN apt install net-tools
#RUN apt install -y mysql-client
#RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

#    RUN ["/bin/bash", "-c", "echo human"]
#    RUN ["/bin/bash", "-c", "docker-php-ext-install mysqli"]
#RUN ["/bin/bash", "-c", "apachectl restart"]

    CMD ["/bin/bash", "-c"]
EXPOSE 80 443

# inside php container:
# docker-php-ext-install mysqli
# apachectl restart
#command: tail -f /dev/null