FROM debian:bullseye

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
vim zsh curl wget git \
python3 python3-pip python3-venv \
&& apt-get clean

# Set zsh as the default shell
RUN chsh -s $(which zsh)

# Install Oh My Zsh for a better shell experience
RUN wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
RUN chmod +x install.sh && yes | ./install.sh
RUN rm install.sh && mkdir /root/lab

COPY ./zshrc /root/.zshrc
# COPY ./zsh_history /root/.zsh_history
COPY ./lab /root/lab

CMD ["tail", "-f", "/dev/null"]
