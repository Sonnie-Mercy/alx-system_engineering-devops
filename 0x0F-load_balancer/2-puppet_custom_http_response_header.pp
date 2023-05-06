# Define the custom header value
$hostname = $facts['hostname']

# Install Nginx
class { 'nginx': }

# Add custom HTTP header
file { '/etc/nginx/sites-available/default':
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $hostname;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }
}
",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
}
