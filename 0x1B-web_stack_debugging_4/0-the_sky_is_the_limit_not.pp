# increases worker processes and restarts nginx

exec {'increase_worker_processes':
  command => "sed -i 's/worker_connections.*/worker_connections 1024;/' /etc/nginx/nginx.conf",
  onlyif  => "grep -q 'worker_connections 1024;' /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin']
  notify  => Exec['restart_nginx'],
}

exec {'restart_nginx':
  command => 'sudo service nginx restart',
  onlyif  => 'sudo nginx -t',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin']
}
