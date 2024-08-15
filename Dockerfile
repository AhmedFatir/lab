FROM debian:bullseye

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y netcat vim nginx zsh curl wget git iputils-ping \
    python3 python3-pip python3-venv \
    procps apt-utils net-tools tree

# Set zsh as the default shell
RUN chsh -s $(which zsh)

# Install Oh My Zsh for a better shell experience
RUN wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
RUN chmod +x install.sh && yes | ./install.sh
RUN rm install.sh && mkdir /root/lab

COPY ./zshrc /root/.zshrc
COPY ./zsh_history /root/.zsh_history

# Install Django globally
RUN pip3 install django
RUN pip3 install django-allauth
RUN pip3 install requests
RUN pip3 install PyJWT
RUN pip3 install crpytography

# Keep the container running
CMD ["tail", "-f", "/dev/null"]
