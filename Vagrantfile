# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX_NAME = "debian/buster64"
BOX_VERSION = "10.4.0"
DISK_SIZE = "20GB"

BOX_IP_PREFIX="172.29.44.10"

Vagrant.configure("2") do |config|
    config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "/tmp/authorized_keys"

    config.vm.define "aaa" do |node|
      node.vm.box = BOX_NAME
      node.vm.box_version = BOX_VERSION
      node.disksize.size = DISK_SIZE

      node.vm.hostname = "aaa"
      node.vm.network "private_network", ip: "#{BOX_IP_PREFIX}1"

      node.vm.provision "shell", inline: "apt-get --allow-releaseinfo-change update", privileged: true
      node.vm.provision "shell", inline: "apt-get install -y openssh-server", privileged: true
      node.vm.provision "shell", inline: "mkdir -p /root/.ssh", privileged: true
      node.vm.provision "shell", inline: "cp /tmp/authorized_keys /root/.ssh/", privileged: true

      node.vm.provider "virtualbox" do |vb|
        vb.memory = "8000"
        vb.cpus = "4"
      end
    end
end
