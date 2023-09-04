# custom_nginx_header.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to get the server's hostname
$server_hostname = $facts['hostname']

# Define an Nginx configuration file that adds the custom header
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # Custom HTTP response header
    add_header X-Served-By $server_hostname;

}",
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
}

# Remove the default Nginx default configuration (if needed)
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-enabled/custom_header'],
}
