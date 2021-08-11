FROM nginx:latest
USER root
COPY ./mscript.sh /
RUN chmod +x /mscript.sh
CMD ["/bin/bash", "-c", "/mscript.sh"]
EXPOSE 80 