# increases the file descriptor limits for the holberton user so they can open files without error

# increase hard file limit
exec { 'increase_hard_file_limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# increase soft file limit
exec { 'increase_soft_file_limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
