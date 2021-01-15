# Hands-on Setup

## Part 1 - Build the Infrastructure

- Get to the AWS Console and spin-up 3 EC2 Instances with ```Red Hat Enterprise Linux 8``` AMI.

- Configure the security groups as shown below:

    - Controller Node ----> Port 22 SSH

    - Target Node1 -------> Port 22 SSH, Port 80 HTTP

    - Target Node2 -------> Port 22 SSH, Port 80 HTTP

## Part 2 - Install Ansible on the Controller Node

- Connect to your ```Controller Node```.

- Optionally you can connect to your instances using VS Code.

                    -------------------- OPTIONAL BELOW ----------------------

- You can also use connect to the Controller Node via VS Code's ```Remote SSH``` Extension. 

- Open up your VS Code editor. 

- Click on the ```Extensions``` icon. 

- Write down ```Remote - SSH``` on the search bar. 

- Click on the first option on the list.

- Click on the install button.

- When the extension is installed, restart your editor.

- Click on the green button (```Open a Remote Window``` button) at the most bottom left.

- Hit enter. (```Connect Current Window to Host...```)

- Enter a name for your connection on the input field and click on ```Add New SSH Host``` option.

- Enter your ssh connection command (```ssh -i <YOUR-PEM-FILE> ec2-user@<YOUR SERVER IP>```) on the input field and hit enter.

- Hit enter again.

- Click on the ```connect``` button at the bottom right.

- Click on ```continue``` option.

- Click on the ```Open Folder``` button and then click on the ```Ok``` button.

- Lastly, open up a new terminal on the current window.

                    -------------------- OPTIONAL ABOVE ----------------------


- to pretend to be disconnected

```bash
$ echo 'ClientAliveInterval 60' | sudo tee --append /etc/ssh/sshd_config
$ sudo service sshd restart
```

- Run the commands below to install Python3 and Ansible. 

```bash
$ sudo yum install -y python3 
```

```bash
$ pip3 install --user ansible
```

- Check Ansible's installation with the command below.

```bash
$ ansible --version
--------------------
Alternatif ansible yükleme
------------------------

## Part 1 - Install Ansible

 
- Spin-up 3 Amazon Linux 2 instances and name them as:
    1. control node
    2. node1 ----> (SSH PORT 22, HTTP PORT 80)
    3. node2 ----> (SSH PORT 22, HTTP PORT 80)


- Connect to the control node via SSH and run the following commands.

```bash
sudo yum update -y
sudo amazon-linux-extras install ansible2
```

### Confirm Installation

- To confirm the successful installation of Ansible, run the following command.
 
```bash
$ ansible --version
```
Stdout:
```
ansible 2.9.12
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/ec2-user/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.18 (default, Aug 27 2020, 21:22:52) [GCC 7.3.1 20180712 (Red Hat 7.3.1-9)]
```
 
- Explain the lines above:
    1. Version Number of Ansible
    2. Path for the Ansible Config File
    3. Modules are searched in this order
    4. Ansible's Python Module path
    5. Ansible's executable file path
    6. Ansible's Python version with GNU Compiler Collection for Red Hat

- Run the command below to transfer your pem key to your Ansible Controller Node.

```bash
$ scp -i <PATH-TO-PEM-FILE> <PATH-TO-PEM-FILE> ec2-user@<CONTROLLER-NODE-IP>:/home/ec2-user
```
[ec2-user@ip-172-31-31-58 ~]$ ll

-rw-rw-r-- 1 ec2-user ec2-user 1704 Jan  8 23:11 ansible.pem

sudo chmod 700 ansible.pem

-rwx------ 1 ec2-user ec2-user 1704 Jan  8 23:11 ansible.pem


## Part 3 - Pinging the Target Nodes


- Make a directory named ```project``` under the home directory and cd into it.

```bash 
$ mkdir project
$ cd project
```

- Create a file named ```inventory.txt``` with the command below.

```bash
$ vi inventory.txt
```

- Paste the content below into the inventory.txt file.

- Along with the hands-on, public or private IPs can be used.

```txt
[webservers]
node1 ansible_host=<node1_ip> ansible_user=ec2-user

[ubuntuservers]
node2 ansible_host=<node2_ip> ansible_user=ubuntu

[all:vars]
ansible_ssh_private_key_file=/home/ec2-user/<pem file>
```
### Configure Ansible on the Control Node

- Connect to the control node for building a basic inventory.

- Edit ```/etc/ansible/hosts``` file by appending the connection information of the remote systems to be managed.

- Along with the hands-on, public or private IPs can be used.

 
```bash
$ sudo su
$ cd /etc/ansible
$ ls 
$ vim hosts 
[webservers]
node1 ansible_host=<node1_ip> ansible_user=ec2-user 
node2 ansible_host=<node2_ip> ansible_user=ec2-user 

[all:vars] #ansible da iki tane grup şekli var birisi all ve ungroup (gruba almadığımız dbservers vs.. serverlar) burada yapılan değişken tanımlamak.

ansible_ssh_private_key_file=/home/ec2-user/<pem file>
```


- Explain what ```ansible_host```, ```ansible_user``` and ansible_ssh_key_file parameters are. For this reason visit the Ansible's [inventory parameters web site](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters).

- Explain what an ```alias``` (node1 and node2) is and where we use it.

- Explain what ```[webservers] and [all:vars]``` expressions are. Elaborate the concepts of [group name](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#inventory-basics-formats-hosts-and-groups), [group variables](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#assigning-a-variable-to-many-machines-group-variables) and [default groups](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#default-groups). 

- Visit the above links for helping to understand the subject. 



scp -i ansible.pem ansible.pem ec2-user@<public DNS name of Control Node>:/home/ec2-user

- Copy your pem file to the /etc/ansible/ directory. First, go to your pem file directory on your local PC and run the following command.

```bash

$ scp -i <pem file> <pem file> ec2-user@<public DNS name of Control Node>:/home/ec2-user
```
- Check if the file is transferred to the remote machine. 



- As an alternative way, create a file on the control node with the same name as the <pem file> in ```/etc/ansible``` directory. 

- Then copy the content of the pem file and paste it in the newly created pem file on the control node.


- ping the nodes 
```bash
$ ansible all -m ping
```

```bash
$ ansible all -m ping -i inventory.txt
```

- Create another file named ```ansible.cfg``` in the "project" directory.

```
[defaults]
host_key_checking = False
inventory=inventory.txt
interpreter_python=auto_silent
```

```bash
$ ansible all -m ping
```
## Part 2 - Ansible Ad-hoc Commands

- To confirm that all our hosts are located by Ansible, we will run the commands below.


```bash
$ ansible all --list-hosts


$ ansible webservers --list-hosts

- To make sure that all our hosts are reachable, we will run various ad-hoc commands that use the ping module.

```bash
$ ansible webservers -m ping
$ ansible node1 -m ping

```
- Explain the content of the output. 

- Go back to the hosts file and change an ip address for showing the negative output.


### Let's Run Some Ad-hoc Commands

- "ansible-doc <module_name>" command is used for seeing the explanation and examples of a specific module.
 
- Run the below command.

```bash
$ ansible-doc ping
```
- Emphasize that the successful pinging returns ```pong``` answer. 

- Ask students how it is possible to ping without opening the ICMP port.

- Show how the ```ansible-doc ping``` command's explanation clarifies the above question.

- Run the command below.
```bash
$ ansible all -m ping
```

```bash
$ ansible all -m ping -o
```

- Explain what ```-o``` option does.
- Run the command below.

```bash
$ ansible --help
```

- Show ```-o``` option on the screen. Also show the meanings of ```-a, -m, -i, --list-hosts, --become-user```.

- Run the command below.

```bash
$ ansible webservers -a "uptime" 

web_server1 | CHANGED | rc=0 >>

 13:00:59 up 42 min,  1 user,  load average: 0.08, 0.02, 0.01
```

- Explain how much the system is up and what is load avarage.

- Numbers for load avarage respectively mean (

load average over the last 1 minute: 8%

load average over the last 5 minutes: 2%

load average over the last 15 minutes: 1%

)

- Run the command below.

```bash
$ ansible webservers -m shell -a "systemctl status sshd"
```
- Explain the output.


- Run the command below.
```bash
$ ansible webservers -m command -a 'df -h'
```
- Then run the same command without ```-m command``` part.

```bash
$ ansible webservers -a 'df -h'
```

- Mention about the fact that the default ad-hoc module is the command module.

- Run the commands below for explaining how to transfer a file.

```bash
$ vi testfile    # Create a text file name "testfile"
  "This is a test file."
```

```bash
$ ansible webservers -m copy -a "src=/home/ec2-user/testfile dest=/home/ec2-user/testfile" 
$ ansible node1 -m shell -a "echo Hello Clarusway > /home/ec2-user/testfile2 ; cat testfile2"

ansible ubuntuservers -m copy -a "src=/home/ec2-user/testfile dest=/home/ubuntu/testfile"
```

- Connect to Node1 and show the files and their content.

ansible node1 -m shell -a "cat testfile"
ansible node2 -m shell -a "cat testfile"

### Go on with Ubuntu 

$ ansible all -m shell -a "echo Hello Clarusway > /home/ubuntu/testfile3"
```
- Explain the error below. Emphasize that the infrastructures we provision need different configurations.

```bash
web_server1 | FAILED | rc=1 >>
/bin/sh: /home/ubuntu/testfile3: No such file or directorynon-zero return code
web_server2 | CHANGED | rc=0 >>
```

- So refactor the commands as shown below.

```bash
$ ansible node2 -m shell -a "echo Hello Clarusway > /home/ubuntu/testfile3"
$ ansible node1:node2 -m shell -a "echo Hello Clarusway > /home/ec2-user/testfile3; echo Hello Clarusway > /home/ubuntu/testfile4"
```

- Emphasize the ```:``` sign between the hosts.


### Using Shell Module

- Run the command below.

```bash
$ ansible webservers -b -m shell -a "yum -y update ; yum -y install nginx ; service nginx start; systemctl enable nginx" 
``` 
- If the above command gives an error complaining about the existance of the package, try the command below.

```bash
ansible webservers -b -m shell -a "amazon-linux-extras install -y nginx1 ; systemctl start nginx ; systemctl enable nginx" 
```

- Run the command below to remove the nginx package.

```bash
$ ansible webservers -b -m shell -a "yum -y remove nginx"
```

- Run the commands below for Ubuntu server

```bash
$ ansible node2 -b -m shell -a "apt update -y ; apt-get install -y nginx ; systemctl start nginx; systemctl enable nginx"
```
 ansible node2 -b -m shell -a "apt-get purge nginx nginx-common -y"

- Visit both of the ip addresses to see the default nginx pages.


### Using Yum and Package Module

- Run the command below.

```bash
$ ansible-doc yum

$ ansible-doc apt

```

- Emphasize the description part of the yum command.

- Show the examples part of the result page.

- Emphasize the fact that these examples are given to be used in ```playbook files```.

- Run the command below ```twice```.

```bash
$ ansible webservers -b -m yum -a "name=nginx state=present"    
```

-  Explain the difference of the standard outputs. Emphasize the changes in color and ```changed``` property together with idempotency. 

- Run the command below.

```bash
$ ansible -b -m package -a "name=nginx state=present" all
```

- Connect to nodes and check if nginx was installed. (nginx -v)

- Explain the difference of ```yum``` and ```package``` modules.
https://docs.ansible.com/ansible/2.8/modules/package_module.html


```bash
$ ansible -b -m package -a "name=nginx state=absent" all
```

ansible all -b -a "systemctl stop nginx" (Bu komut çalıştı)
ansible all -b -m package -a "name=nginx state=absent" (Bu komutla kaldırmadı)

çalıştırarak nginx leri kaldır. installation için -b komutuyla çalıştırmak lazım. Hata veriyor nginx

```
Part 2 - Ansible Playbooks

- Create a yaml file named "playbook1.yml" and make sure all our hosts are up and running.

```bash
---
- name: Test Connectivity
  hosts: all
  tasks:
   - name: Ping test
     ping:
```

codebeautify.org/yaml-validator sitesinden kontrol yapılabilir.

- Run the yaml file.

```bash
ansible-playbook playbook1.yml
```


- Create a text file named "testfile1" and write "Hello Clarusway" with using vim. Then create a yaml file name "playbook2.yml" and send the "testfile1" to the hosts. 

```yml
---
- name: Copy for linux
  hosts: webservers
  tasks:
   - name: Copy your file to the webservers
     copy:
       src: /home/ec2-user/testfile1
       dest: /home/ec2-user/testfile1

- name: Copy for ubuntu
  hosts: ubuntuservers
  tasks:
   - name: Copy your file to the ubuntuservers
     copy:
       src: /home/ec2-user/testfile1
       dest: /home/ubuntu/testfile1

```

- Run the yaml file.

```bash
ansible-playbook playbook2.yml
```
ansible all -a "ls"

cat komutuyla içine bakabilirsin ansible node1 -m shell -a "cat testfile1"

- Connect the nodes with SSH and check if the text files are copied or not. 

- Create a yaml file named playbook3.yml as below.

```bash
$ vim playbook3.yml

```yml
- name: Copy for linux
  hosts: webservers
  tasks:
   - name: Copy your file to the webservers
     copy:
       src: /home/ec2-user/testfile1
       dest: /home/ec2-user/testfile1
       mode: u+rw,g-wx,o-rwx

- name: Copy for ubuntu
  hosts: ubuntuservers
  tasks:
   - name: Copy your file to the ubuntuservers
     copy:
       src: /home/ec2-user/testfile1
       dest: /home/ubuntu/testfile1
       mode: u+rw,g-wx,o-rwx

- name: Copy for node1
  hosts: node1
  tasks:
   - name: Copy using inline content
     copy:
       content: '# This file was moved to /etc/ansible/testfile1'
       dest: /home/ec2-user/testfile2

   - name: Create a new text file
     shell: "echo Hello World > /home/ec2-user/testfile3"
```
- Run the yaml file.

```bash
ansible-playbook playbook3.yml
```
- Connect the node1 with SSH and check if the text files are there.

- Install Apache server with "playbook4.yml". After the installation, check if the Apache server is reachable from the browser.


$ vim playbook4.yml

---
- name: Apache installation for webservers
  hosts: webservers
  tasks:
   - name: install the latest version of Apache
     yum:
       name: httpd
       state: latest

   - name: start Apache
     shell: "service httpd start"

- name: Apache installation for ubuntuservers
  hosts: ubuntuservers
  tasks:
   - name: install the latest version of Apache
     apt:
       name: apache2
       state: latest
```
- Run the yaml file.

```bash
$ ansible-playbook -b playbook4.yml
$ ansible-playbook -b playbook4.yml   # Run the command again and show the changing parts of the output.
```

- Create playbook5.yml and remove the Apache server from the hosts.

```bash
$ vim playbook5.yml

---
- name: Remove Apache from webservers
  hosts: webservers
  tasks:
   - name: Remove Apache
     yum:
       name: httpd
       state: absent

- name: Remove Apache from ubuntuservers
  hosts: ubuntuservers
  tasks:
   - name: Remove Apache
     apt:
       name: apache2
       state: absent
   - name: Remove unwanted Apache2 packages from the system
     apt:
       autoremove: yes
       purge: yes
```

- Run the yaml file.

```bash
$ ansible-playbook -b playbook5.yml
```

- This time, install Apache and wget together with playbook6.yml. After the installation, enter the IP-address of node2 to the browser and show the Apache server. Then, connect node1 with SSH and check if "wget and apache server" are running. 

```bash
vim playbook6.yml

---
- name: play 6
  hosts: ubuntuservers
  tasks:
   - name: installing apache
     apt:
       name: apache2
       state: latest

   - name: index.html
     copy:
       content: "<h1>Hello Clarusway</h1>"
       dest: /var/www/html/index.html

   - name: restart apache2
     service:
       name: apache2
       state: restarted
       enabled: yes

- name: play 5
  hosts: webservers
  tasks:
    - name: installing httpd and wget
      yum:
        pkg: "{{ item }}"
        state: present
      with_items:
        - httpd
        - wget
        #pkg: ['httpd', 'wget']
        #state: present
```
uyarı veriyor verdiği uyarıyı gidermek için 
pkg: ['httpd', 'wget']
şeklinde kullanınca hata vermiyor.
with_items loop un yerine geçiyor.
- Run the yaml file.

```bash
ansible-playbook -b playbook6.yml
```

- Remove Apache and wget from the hosts with playbook7.yml.

```bash
vim playbook7.yml

---
- name: play 6
  hosts: ubuntuservers
  tasks:
   - name: Uninstalling Apache
     apt:
       name: apache2
       state: absent
       update_cache: yes
   - name: Remove unwanted Apache2 packages
     apt:
       autoremove: yes
       purge: yes

- name: play 7
  hosts: webservers
  tasks:
   - name: removing apache and wget
     yum:
       pkg: "{{ item }}"
       state: absent
     with_items:
       - httpd
       - wget
      #pkg: ['httpd', 'wget']
      #state: absent
```

- Run the yaml file.

```bash
ansible-playbook -b playbook7.yml
```

- Using ansible loop and conditional, create users with playbook8.yml. 

```bash
vi playbook8.yml
```

```bash
---
- name: Create users
  hosts: "*"
  tasks:
    - user:
        name: "{{ item }}"
        state: present
      loop:
        - joe
        - matt
        - james
        - oliver
      when: ansible_os_family == "RedHat"

    - user:
        name: "{{ item }}"
        state: present
      loop:
        - david
        - tyler
      when: ansible_os_family == "SUSE"

    - user:
        name: "{{ item }}"
        state: present
      loop:
        - john
        - aaron
      when: ansible_os_family == "Debian" or ansible_os_family == "20.04"

```

- Run the playbook8.yml

```bash
ansible-playbook -b playbook8.yml
```
 * all demek loop  işletim sistemi redhat ise çalıştır önce condition lara bakıyor, ilk yaptığı gathering facts bilgileri topluyor. 


ansible_os family yi göster topluyor 
ansible all -a "cat /etc/passwd"



## Part 2 - Ansible Facts

- Gathering Facts

```bash
$ ansible all -m setup
```
```
ec2-34-201-69-79.compute-1.amazonaws.com | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.31.20.246"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::88c:37ff:fe8f:3b71"
        ],
        "ansible_apparmor": {
            "status": "disabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "08/24/2006",
        "ansible_bios_vendor": "Xen",
        "ansible_bios_version": "4.2.amazon",
        "ansible_board_asset_tag": "NA",
        "ansible_board_name": "NA",
        "ansible_board_serial": "NA",
```
 
- create a playbook named "facts.yml"

```yml
- name: show facts
  hosts: all
  tasks:
    - name: print facts
      debug:
        var: ansible_facts
```
- run the play book

```bash
$ ansible-playbook facts.yml
```

- create a playbook named "ipaddress.yml"

```yml
- hosts: all
  tasks:
  - name: show IP address
    debug:
      msg: >
       This host uses IP address {{ ansible_facts.default_ipv4.address }}

```

debug modülüne bakabilirsin. 
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html


- run the playbook

## Part 3 - Working with sensitive data

- Create encypted variables using "ansible-vault" command

```bash
ansible-vault create secret.yml
```

New Vault password: xxxx
Confirm Nev Vault password: xxxx

```yml
username: tyler
password: 99abcd
```

- look at the content

```bash
$ cat secret.yml
```
```
33663233353162643530353634323061613431366332373334373066353263353864643630656338
6165373734333563393162333762386132333665353863610a303130346362343038646139613632
62633438623265656330326435646366363137373333613463313138333765366466663934646436
3833386437376337650a636339313535323264626365303031366534363039383935333133306264
61303433636266636331633734626336643466643735623135633361656131316463
```
- how to use it:

- create a file named "create-user"

```bash
$ vi create-user.yml

```

```yml
- name: create a user
  hosts: all
  become: true
  vars_files:
    - secret.yml
  tasks:
    - name: creating user
      user:
        name: "{{ username }}"
        password: "{{ password }}"
```

- run the plaaybook

```bash
ansible-playbook create-user.yml
```
```bash
ERROR! Attempting to decrypt but no vault secrets found

Script dosyada çalışırken aşağıdaki komutu çalıştır.
```
- Run the playbook with "--ask-vault-pass" command:

```bash
$ ansible-playbook --ask-vault-pass create-user.yml
```
Vault password: xxxx

```
PLAY RECAP ******************************************************************************************
node1                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
node2                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```



- To verrify it

```bash
ansible all -b -m command -a "grep tyler /etc/shadow"
```
```
node1 | CHANGED | rc=0 >>
tyler:99abcd:18569:0:99999:7:::
```

- ansible-vault create secret1.yml


- Create another encypted variables using "ansible-vault" command but this time use SHA (Secure Hash Algorithm) for your password:
 HArfli olursa hata olabiliyor.
```bash
ansible-vault create secret-1.yml
```

New Vault password: xxxx
Confirm Nev Vault password: xxxx

```yml
username: Oliver
pwhash: 14abcd
```

- look at the content

```bash
$ cat secret1.yml
```
```
33663233353162643530353634323061613431366332373334373066353263353864643630656338
6165373734333563393162333762386132333665353863610a303130346362343038646139613632
62633438623265656330326435646366363137373333613463313138333765366466663934646436
3833386437376337650a636339313535323264626365303031366534363039383935333133306264
61303433636266636331633734626336643466643735623135633361656131316463
```
- how to use it:

create-user
```bash
$ vi create-user-1.yml

```

```yml
- name: create a user
  hosts: all
  become: true
  vars_files:
    - secret-1.yml
  tasks:
    - name: creating user
      user:
        name: "{{ username }}"
        password: "{{ pwhash | password_hash ('sha512') }}"
```

- run the plaaybook


```bash
$ ansible-playbook --ask-vault-pass create-user-1.yml
```
Vault password: xxxx

```
PLAY RECAP ******************************************************************************************
node1                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
node2                      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

- to verrify it:

```bash
ansible all -b -m command -a "grep tyler /etc/shadow"
```
```
node1 | CHANGED | rc=0 >>
tyler:#665fffgkg6&fkg689##2£6466?%^^+&%+:18569:0:99999:7:::
```