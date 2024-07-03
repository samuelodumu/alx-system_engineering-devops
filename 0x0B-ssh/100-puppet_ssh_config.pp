# doing task 2 with puppet

file_line { 'configuring /etc/ssh/ssh_config':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  ensure => 'present',
}
file_line { 'adding another line':
  path   =>  '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => 'present',
}
