# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://sonniemercy.tech/;
    }
}",
  require => Package['nginx'],
}

# Create custom index.html file
file { '/var/www/html/index.html':
  ensure => file,
  content => '<html><body>Hello World!</body></html>',
}
