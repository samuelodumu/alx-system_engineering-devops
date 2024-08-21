# increases worker processes and restarts nginx

exec {'raise_system_limits':
  command => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 102400\"/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
  notify  => Exec['restart_nginx'],
}

exec {'restart_nginx':
  command => 'sudo service nginx restart',
  onlyif  => 'sudo nginx -t',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin']
}
