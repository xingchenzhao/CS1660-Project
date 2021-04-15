FROM python
COPY . /ds_gui
WORKDIR /ds_gui
RUN apt-get update && \
    apt-get upgrade -y 

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox
RUN apt update && apt install -y git xterm spyder3
CMD ["python","app.py"]