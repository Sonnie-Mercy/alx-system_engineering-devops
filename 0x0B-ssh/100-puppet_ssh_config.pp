#!/usr/bin/env bash
# using puppet
file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
Host *
    IdentityFile /root/.ssh/school
    PasswordAuthentication no
  ",
}
