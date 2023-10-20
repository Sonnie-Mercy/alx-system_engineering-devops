# Adjust the file limits for the user 'holberton' to enable smooth login and file access.

# Increase the hard file limit for the 'holberton' user.
exec { 'increase-hard-file-limit-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limit for the 'holberton' user.
exec { 'increase-soft-file-limit-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
