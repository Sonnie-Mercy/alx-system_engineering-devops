# kill me now
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => '/usr/bin',
  provider  => shell,
}
