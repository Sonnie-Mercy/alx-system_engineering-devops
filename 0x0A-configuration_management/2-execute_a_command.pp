# kill me now
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
  provider  => shell,
}
