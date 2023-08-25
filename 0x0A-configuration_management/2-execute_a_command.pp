# This manifest kills a process named "killmenow" using the exec resource and pkill command.

exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/usr/local/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
