file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
Host ubuntu@100.25.138.158
    IdentityFile /root/.ssh/school
    PasswordAuthentication no
  ",
}
