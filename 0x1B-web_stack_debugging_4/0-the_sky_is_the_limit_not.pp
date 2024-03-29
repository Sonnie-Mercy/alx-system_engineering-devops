# Increase the amount of traffic an Nginx server can handle

# Modify the default file to increase ULIMIT
file { '/etc/default/nginx':
  ensure  => file,
  content => 'ulimit -n 4096',
}

# Notify the service to restart on file change
service { 'nginx':
  ensure    => 'running',
  subscribe => File['/etc/default/nginx'],
}
