file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
Host your_server_ip
    IdentityFile /root/.ssh/school
    PasswordAuthentication no
  ",
}
