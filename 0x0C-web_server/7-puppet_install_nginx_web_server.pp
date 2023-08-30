package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/redirect_me/index.html':
  ensure => 'file',
  content => 'Redirecting to another page...',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location /redirect_me {
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
",
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => [Package['nginx'], File['/etc/nginx/sites-available/default']],
  subscribe => File['/etc/nginx/sites-available/default'],
}
