saia-flow
=========

This role supports the installation and configuration of the "saia-flow" solution.

The role will:
  1. install all required packages
  2. Create required directories
  3. Deploy rclone.conf to support the FTP process
  4. Deploy supporting scripts
  5. Deploy a rc.local execution file
  6. Deploy rc-local.service definition
  7. Enable the rc-local service
  8. If the changes requires it, reboot the server 
  9. Make sure rc-local service is running/started
  10. Make sure rc-local service is restarted if changed
  
Requirements
------------

This solution expects the Mettler Dimensioner running Ubuntu Server 20.04 and an available installation of InfluxDB.

Role Variables
--------------
  # default vars in defaults/main.yml
    
    # influxbd
    influxdb_token: aoWOrJjPawxYWj_x3QAQVX2AzAH6Bn9ev2M74yGFvn-vRJZcElsVCUCp7YnX7UJsGwyleYwkSGsMtibcKhPkkw==
    influxdb_url: http://100.64.47.154:8086/api/v2/write

    # file system directories
    rclone_dir: /root/.config/rclone/
    base_dir: /opt/saia_flow
    incoming_dir: /opt/saia_flow/incoming/
    processed_dir: /opt/saia_flow/processed/
    errors_dir: /opt/saia_flow/errors/

    directory_list:
      - "{{ rclone_dir }}"
      - "{{ base_dir }}"
      - "{{ incoming_dir }}"
      - "{{ processed_dir }}"
      - "{{ errors_dir }}"

    # scripts
    watch_incoming_sh: "{{ base_dir }}/watch-incoming.sh"
    influxdb_sh: "{{ base_dir }}/post2InfluxDB.sh"

    # packages to deploy
    package_list:
        - vsftpd=3.0.3-12
        - inotify-tools=3.14-8
        - rclone=1.50.2-2
        - openssl=1.1.1f-1ubuntu2.10
        - ssl-cert=1.0.39

    # rclone FTP server
    ftp_host: 100.64.47.154
    ftp_user: anonymous
    ftp_port: 21
    ftp_pass: odSAK0Fe4SX8wyCdL2cHrmx8DdyV_nZMWY1M3A
    ftp_tls: false
    ftp_concurrency: 0
    ftp_no_check_certificate: true# influxbd
    influxdb_token: aoWOrJjPawxYWj_x3QAQVX2AzAH6Bn9ev2M74yGFvn-vRJZcElsVCUCp7YnX7UJsGwyleYwkSGsMtibcKhPkkw==
    influxdb_url: http://100.64.47.154:8086/api/v2/write

    # file system directories
    rclone_dir: /root/.config/rclone/
    base_dir: /opt/saia_flow
    incoming_dir: /opt/saia_flow/incoming/
    processed_dir: /opt/saia_flow/processed/
    errors_dir: /opt/saia_flow/errors/

    directory_list:
      - "{{ rclone_dir }}"
      - "{{ base_dir }}"
      - "{{ incoming_dir }}"
      - "{{ processed_dir }}"
      - "{{ errors_dir }}"

    # scripts
    watch_incoming_sh: "{{ base_dir }}/watch-incoming.sh"
    influxdb_sh: "{{ base_dir }}/post2InfluxDB.sh"

    # packages to deploy
    package_list:
        - vsftpd=3.0.3-12
        - inotify-tools=3.14-8
        - rclone=1.50.2-2
        - openssl=1.1.1f-1ubuntu2.10
        - ssl-cert=1.0.39

    # rclone FTP server
    ftp_host: 100.64.47.154
    ftp_user: anonymous
    ftp_port: 21
    ftp_pass: odSAK0Fe4SX8wyCdL2cHrmx8DdyV_nZMWY1M3A
    ftp_tls: false
    ftp_concurrency: 0
    ftp_no_check_certificate: true

Dependencies
------------

No additional Ansible dependancies

Example Playbook
----------------

  # site.yml
  ---
  - name: Install Saia Flow on Dimensioners
    hosts: [dimensioners]

    roles:
    - saia-flow 
    
  # main.yml
  ---
  - name: install saia-flow (may require reboot)
    include_tasks: install.yml

License
-------

BSD

Author Information
------------------

Thomas Gould
