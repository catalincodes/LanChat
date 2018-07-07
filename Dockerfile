# our base image
FROM centos:7

# Install python and pip
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u
RUN yum -y install python36u-pip
RUN yum -y install python36u-devel

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
# COPY requirements.txt /usr/src/app/
# RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY chat.py /usr/src/app/
#COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 12000

# run the application
CMD ["python3.6", "/usr/src/app/chat.py"]