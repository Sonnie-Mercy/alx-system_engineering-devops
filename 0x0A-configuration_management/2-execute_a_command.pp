# kill me now
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  path    => '/usr/bin',
  provider  => shell,
}
