# sx_trap_fwd container

FROM ubuntu:bionic
RUN apt update && apt --no-install-recommends -y install python

WORKDIR /
COPY ./sx_trap_fwd.py /usr/bin/
CMD ["python", "/usr/bin/sx_trap_fwd.py"]
