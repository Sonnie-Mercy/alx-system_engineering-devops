# kill me now
exec { 'kill process':
  command => 'pkill  -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => ['/usr/local/bin', '/usr/bin'],
}
