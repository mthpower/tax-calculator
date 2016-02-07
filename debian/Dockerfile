# ----------------------------------------------------------------------------#
# This Dockerfile creates a Debian package for the `tax-calculator` CLI.      #
#                                                                             #
# Usage: cd .. && make dpkg                                                   #
# ----------------------------------------------------------------------------#
FROM ubuntu:14.04
MAINTAINER Matthew Power <matthew@mthpower.uk>

RUN apt-get update && apt-get install -y -qq python-software-properties software-properties-common
RUN add-apt-repository ppa:spotify-jyrki/dh-virtualenv
RUN apt-get update && apt-get install -y -qq build-essential debhelper devscripts equivs

ADD ./ /root/tax-calculator

RUN mk-build-deps -i /root/tax-calculator/debian/control --tool "apt-get -y -qq"

RUN mkdir /mnt/dist
VOLUME /mnt/dist

WORKDIR /root/tax-calculator

ENV DH_VIRTUALENV_INSTALL_ROOT /opt/tax-calculator/
ENV DESTINATION_DPKG_DIR /mnt/dist/
CMD ["dpkg-buildpackage", "-us", "-uc", "-b", "--changes-option=-u/mnt/dist/"]
